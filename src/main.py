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

cldump = ClassicalRegister(4, 'cldump')
qdump = QuantumRegister(4,'qdump')

bus = QuantumRegister(4, 'b')

qc = QuantumCircuit(c1,c2,c3,s1,s2,s3,h1,h2,h3,i1,i2,i3,bus,cldump,qdump)

def bus_in(register):
    for i in range(4):
        qc.swap(register[i], bus[i])

def bus_out(register):
    for i in range(4):
        qc.swap(register[i], bus[i])