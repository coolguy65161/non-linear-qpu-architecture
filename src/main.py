from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

c1 = QuantumRegister(4, 'c1')
c2 = QuantumRegister(4, 'c2')
c3 = QuantumRegister(4, 'c3')

s1 = QuantumRegister(4, 's1')
s2 = QuantumRegister(4, 's2')
s3 = QuantumRegister(4, 's3')

h1 = QuantumRegister(4, 'h1')
h2 = QuantumRegister(4, 'h2')
h3 = QuantumRegister(4, 'h3')

i1 = ClassicalRegister(4, 'i1')
i2 = ClassicalRegister(4, 'i2')
i3 = ClassicalRegister(4, 'i3')

dump = QuantumRegister(4,'dump') #implemented
check = ClassicalRegister(4, 'check') #implemented
bus = QuantumRegister(4, 'b') #implemented

qc = QuantumCircuit(c1,c2,c3,s1,s2,s3,h1,h2,h3,i1,i2,i3,bus,dump,check)

busqueue = []
dumpqueue = []

def reset(qubit, out):
    qc.measure(qubit, out)
    with qc.if_test((out, 1)):
        qc.x(qubit)

def reg_reset(reg):
    for i in range(4):
        reset(reg[i], check[i])

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
    item = busqueue[0]
    regA = item[0]
    regB = item[1]

    transfer(regA, regB)
    busqueue.pop(0)

def add_dumpqueue(reg):
    dumpqueue.append(reg)

def perform_dumpqueue():
    reg = dumpqueue[0]

    transfer(reg, dumpqueue)
    dumpqueue.pop(0)


