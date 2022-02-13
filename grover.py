from typing import Union, List
from math import sqrt, acos, pi

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute
from qiskit.circuit.gate import Gate
from qiskit.circuit.quantumregister import Qubit
from qiskit.providers.aer.backends.aer_simulator import AerSimulator


def phase_oracle(state: str) -> Gate:
    qc: QuantumCircuit = QuantumCircuit(len(state))
    neg_qubits: List[Qubit] = []
    state = state[::-1]
    for i in range(len(state)):
        if (state[i] == "0"):
            neg_qubits.append(qc.qubits[i])

    if neg_qubits:
        qc.x(neg_qubits)
    qc.h(qc.qubits[-1])
    qc.mcx(qc.qubits[:-1], qc.qubits[-1])
    qc.h(qc.qubits[-1])
    if neg_qubits:
        qc.x(neg_qubits)

    gate: Gate = qc.to_gate()
    gate.name = "Oracle"

    return gate


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


def grover() -> None:
    num_qubits: int = 4

    circuit: QuantumCircuit = QuantumCircuit(num_qubits)

    entries = 2**num_qubits
    steps: int = round(acos(1 / sqrt(entries)) / acos((entries - 2) / entries))
    # steps = int((pi/4)*sqrt(entries/1))

    circuit.h(circuit.qubits)

    grover_op: Gate = grover_operator("0111")
    for _ in range(steps):
        circuit.append(grover_op, circuit.qubits)

    circuit.measure_all()
    print(circuit)

    sim = AerSimulator()
    counts = execute(circuit, sim).result().get_counts()

    print(counts)


def grover_diffuser(size: int) -> Gate:
    qc: QuantumCircuit = QuantumCircuit(size)

    qc.h(qc.qubits)
    qc.x(qc.qubits)

    # Make a multi controlled z gate
    qc.h(size - 1)
    qc.mcx(qc.qubits[:-1], size - 1)
    qc.h(size - 1)

    qc.x(qc.qubits)
    qc.h(qc.qubits)

    gate: Gate = qc.to_gate()
    gate.name = "Diffuser"
    return gate


def grover_operator(state: str) -> Gate:
    qc: QuantumCircuit = QuantumCircuit(len(state))
    qc.append(phase_oracle(state), qc.qubits)
    qc.append(grover_diffuser(len(state)), qc.qubits)

    gate: Gate = qc.to_gate()
    gate.name = "G"

    return gate


grover()

