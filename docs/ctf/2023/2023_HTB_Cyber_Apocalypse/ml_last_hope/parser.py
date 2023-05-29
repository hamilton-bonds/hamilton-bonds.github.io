# Importing standard Qiskit libraries
from qiskit import *
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
from qiskit_aer import AerSimulator

# qiskit-ibmq-provider has been deprecated.
# Please see the Migration Guides in https://ibm.biz/provider_migration_guide for more detail.
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Estimator, Session, Options

# Loading your IBM Quantum account(s)
service = QiskitRuntimeService(channel="ibm_quantum")

filename = 'quantum_artifact.qasm'

qc = QuantumCircuit.from_qasm_file(filename)

QASM_string = qc.qasm()

with Session(backend=service.backend("ibmq_qasm_simulator")):
    result = Sampler().run(qc).result()
    
print(result.quasi_dists)

# Convert int to hex and then convert that hex to ascii
