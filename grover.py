from math import sqrt, acos, pi
from typing import List

from qiskit import QuantumCircuit, execute
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


def grover_operator(states: List[str]) -> Gate:
    size: int = len(states[0])
    qc: QuantumCircuit = QuantumCircuit(size)
    for state in states:
        qc.append(phase_oracle(state), qc.qubits)

    qc.append(grover_diffuser(size), qc.qubits)

    gate: Gate = qc.to_gate()
    gate.name = "G"

    return gate


def grover(states: List[str]) -> None:
    num_qubits: int = len(states[0])

    circuit: QuantumCircuit = QuantumCircuit(num_qubits)

    entries = 2**num_qubits
    steps: int = int(acos(1 / sqrt(entries)) / acos((entries - 2) / entries))
    # print(steps)
    # steps = int((pi/4)*sqrt(entries/len(states)))
    # print(steps)
    print(f"Precisão > {(entries - len(states)) / entries}")

    circuit.h(circuit.qubits)

    grover_op: Gate = grover_operator(states)
    for _ in range(steps):
        circuit.append(grover_op, circuit.qubits)

    circuit.measure_all()

    sim = AerSimulator()
    counts = execute(circuit, sim).result().get_counts()

    print(counts)

    return None


grover(["1010", "1000", "0101"])
