from typing import Union, Tuple, List

from qiskit import QuantumCircuit, QuantumRegister


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


def multiple_control_gate(qc: QuantumCircuit,
                          control_qubits: Union[QuantumRegister, List[int]],
                          work_qubits: Union[QuantumRegister, List[int]],
                          target_qubit: Union[QuantumRegister, int]
                          ) -> None:

    num_ctrl_qubits: int = len(control_qubits)
    qc.ccx(control_qubits[0], control_qubits[1], work_qubits[0])

    for i in range(2, num_ctrl_qubits):
        qc.ccx(control_qubit1=control_qubits[i],
               control_qubit2=work_qubits[i - 2],
               target_qubit=work_qubits[i - 1])

    qc.cz(control_qubit=work_qubits[num_ctrl_qubits - 2], target_qubit=target_qubit[0])

    for i in reversed(range(2, num_ctrl_qubits)):
        qc.ccx(control_qubit1=control_qubits[i],
               control_qubit2=work_qubits[i - 2],
               target_qubit=work_qubits[i - 1])

    qc.ccx(control_qubits[0], control_qubits[1], work_qubits[0])

    return None
