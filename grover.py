from math import sqrt, pi, log2, ceil
from typing import List

from qiskit import QuantumCircuit, execute
from qiskit.circuit.gate import Gate
from qiskit.circuit.quantumregister import Qubit
from qiskit.providers.aer.backends.aer_simulator import AerSimulator


def phase_oracle(state: int, size: int) -> Gate:
    state: str = bin(state)[2:]
    while (len(state) < size):
        state = "0" + state
    qc: QuantumCircuit = QuantumCircuit(size)
    flip_qubits: List[Qubit] = []
    state = state[::-1]
    for i in range(len(state)):
        if (state[i] == "0"):
            flip_qubits.append(qc.qubits[i])

    if flip_qubits:
        qc.x(flip_qubits)
    qc.h(qc.qubits[-1])
    qc.mcx(qc.qubits[:-1], qc.qubits[-1])
    qc.h(qc.qubits[-1])
    if flip_qubits:
        qc.x(flip_qubits)

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


def grover_operator(states: List[int], size: int) -> Gate:
    qc: QuantumCircuit = QuantumCircuit(size)
    for state in states:
        qc.append(phase_oracle(state, size), qc.qubits)

    qc.append(grover_diffuser(size), qc.qubits)

    gate: Gate = qc.to_gate()
    gate.name = "G"

    return gate


def grover(states: List[int]) -> int:
    num_qubits: int = ceil(log2(max(states)))

    circuit: QuantumCircuit = QuantumCircuit(num_qubits)

    entries = 2**num_qubits
    steps = int((pi/4)*sqrt(entries/len(states)))

    circuit.h(circuit.qubits)

    grover_op: Gate = grover_operator(states, num_qubits)
    for _ in range(steps):
        circuit.append(grover_op, circuit.qubits)

    circuit.measure_all()

    sim = AerSimulator()
    counts = execute(circuit, sim, shots=1).result().get_counts()

    return int(list(counts)[0], 2)
