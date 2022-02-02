from typing import Tuple, Union

from qiskit import QuantumCircuit, QuantumRegister
from qiskit.providers.aer.backends.aer_simulator import AerSimulator


def create_bell_pair(quantum_circuit: QuantumCircuit,
                     control_qubit: Union[int, QuantumRegister],
                     target_qubit: Union[int, QuantumRegister],
                     state: Tuple[int, int] = (0, 0)
                     ) -> None:
    """
    Returns:
        QuantumCircuit: Circuit that produces a Bell pair
    """
    if state[0]:
        quantum_circuit.x(target_qubit)

    if state[1]:
        quantum_circuit.x(control_qubit)

    quantum_circuit.h(control_qubit)
    quantum_circuit.cx(control_qubit, target_qubit)
    return None


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
quantum_circuit: QuantumCircuit = QuantumCircuit(2)
create_bell_pair(quantum_circuit, 0, 1)
aer_sim = AerSimulator()


alice_encode(quantum_circuit, 1, message)
bob_decode(quantum_circuit)

quantum_circuit.measure_all()
print(quantum_circuit)

result = aer_sim.run(quantum_circuit).result()
counts = result.get_counts()
print(counts)
