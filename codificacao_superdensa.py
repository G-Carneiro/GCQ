from typing import Tuple

from qiskit import QuantumCircuit
from qiskit.providers.aer.backends.aer_simulator import AerSimulator


def create_bell_pair() -> QuantumCircuit:
    """
    Returns:
        QuantumCircuit: Circuit that produces a Bell pair
    """
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    return qc


def alice_encode(qc: QuantumCircuit,
                 qubit: int,
                 message: Tuple[int, int]
                 ) -> None:
    if message[1]:
        qc.x(qubit)

    if message[0]:
        qc.z(qubit)

    return None


def bob_decode(qc: QuantumCircuit) -> None:
    qc.cx(0, 1)
    qc.h(0)

    return None


message = (1, 0)
quantum_circuit: QuantumCircuit = create_bell_pair()
aer_sim = AerSimulator()


alice_encode(quantum_circuit, 1, message)
bob_decode(quantum_circuit)
quantum_circuit.measure_all()
print(quantum_circuit)
result = aer_sim.run(quantum_circuit).result()
counts = result.get_counts()
print(counts)
