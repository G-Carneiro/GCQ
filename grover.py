from math import sqrt, pi
from typing import List

from qiskit import QuantumCircuit, execute, IBMQ, transpile
from qiskit.circuit.gate import Gate
from qiskit.circuit.quantumregister import Qubit
from qiskit.providers.aer.backends.aer_simulator import AerSimulator
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor

IBMQ.enable_account("98e8a2739b6f1ef5e4855f3eb754f84ee240e"
                    "8cd5370de304cffa2f527f47fbe3a398efd98"
                    "6329d655f70a18d3607767474efcf32b72d0f"
                    "3a7dbfadb3e34ee1f")
# Load IBM Q account and get the least busy backend device
provider = IBMQ.get_provider()
device = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= 5
                                                        and not x.configuration().simulator
                                                        and x.status().operational))
print("Running on current least busy device: ", device)
# print(provider.backends())
# backend = provider.get_backend("ibmq_manila")


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


def grover(states: List[int], num_qubits: int) -> int:
    circuit: QuantumCircuit = QuantumCircuit(num_qubits)

    entries = 2 ** num_qubits
    steps = int((pi / 4) * sqrt(entries / len(states)))

    circuit.h(circuit.qubits)

    grover_op: Gate = grover_operator(states, num_qubits)
    for _ in range(steps):
        circuit.append(grover_op, circuit.qubits)

    circuit.measure_all()

    # sim = AerSimulator()
    # counts = execute(circuit, sim, shots=1).result().get_counts()
    # Run our circuit on the least busy backend. Monitor the execution of the job in the queue
    transpiled_grover_circuit = transpile(circuit, device, optimization_level=3)
    job = device.run(transpiled_grover_circuit)
    job_monitor(job, interval=2)
    results = job.result()
    counts = results.get_counts(circuit)

    return int(list(counts)[0], 2)


print(grover([1], 6))
