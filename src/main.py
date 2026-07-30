from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

#implemented
c1 = QuantumRegister(4, 'c1')
c2 = QuantumRegister(4, 'c2')
c3 = QuantumRegister(4, 'c3')

#implemented
s1 = QuantumRegister(4, 's1')
s2 = QuantumRegister(4, 's2')
s3 = QuantumRegister(4, 's3')


h1 = QuantumRegister(4, 'h1')
h2 = QuantumRegister(4, 'h2')
h3 = QuantumRegister(4, 'h3')

#implemented
i1 = ClassicalRegister(4, 'i1')
i2 = ClassicalRegister(4, 'i2')
i3 = ClassicalRegister(4, 'i3')

dump = QuantumRegister(4,'dump') #implemented
check = ClassicalRegister(4, 'check') #implemented
bus = QuantumRegister(4, 'b') #implemented

qc = QuantumCircuit(c1,c2,c3,s1,s2,s3,i1,i2,i3,h1,h2,h3,bus,dump,check)

busqueue = []
dumpqueue = []

# reset

def reset(qubit, out):
    qc.measure(qubit, out)
    with qc.if_test((out, 1)):
        qc.x(qubit)

def reg_reset(reg):
    for i in range(4):
        reset(reg[i], check[i])

# bus

def bus_swap(reg):
    for i in range(4):

        qc.swap(reg[i], bus[i])

def transfer(regA, regB):
    bus_swap(regA)
    bus_swap(regB)
    reg_reset(bus)

def add_busqueue(regA, regB):
    busqueue.append([regA, regB])

def perform_busqueue():
    if len(busqueue) > 0:
        item = busqueue[0]
        regA = item[0]
        regB = item[1]

        transfer(regA, regB)
        busqueue.pop(0)

# dump

def add_dumpqueue(reg):
    dumpqueue.append(reg)

def perform_dumpqueue():
    if len(dumpqueue) > 0:
        reg = dumpqueue[0]
        print(reg)
        transfer(reg, dump)
        reg_reset(dump)
        
        dumpqueue.pop(0)

#i1-i3
def output_reg(c_reg, i_reg):
    for i in range(4):
        qc.measure(c_reg[i], i_reg[i])

def get_output(i_reg):
    info = []
    for i in range(4):
        info.append(i_reg[i])
    return info

#h1-h3

#not in any form of superposition only
def nsp_fan_out(regA, regB, helper):
    for i in range(4):
        qc.cx(regA[i], helper[i])
    add_busqueue(helper, regB)

def clock_tick():
    perform_busqueue()
    perform_dumpqueue()


qc.x(s1[0])
qc.x(s1[1])

add_busqueue(s1, c1)

clock_tick()

qc.cx(c1[0], c1[2]) 

nsp_fan_out(c1, s1, h1)

add_dumpqueue(h1)

clock_tick()

output_reg(c1, i1)

simulator = AerSimulator()

job = simulator.run(qc, shots=1000)
result = job.result()

counts = result.get_counts(qc)

print("=" * 50)
print("QPU SIMULATION COMPLETE!")
print("Information Retriever (i1) Output Counts:")
print(counts)
print("=" * 50)