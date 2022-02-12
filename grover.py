from typing import Union, List
from math import sqrt, acos, pi

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.quantumregister import Qubit
from qiskit.circuit.library import MCMT, ZGate
from qiskit.providers.aer.backends.aer_simulator import AerSimulator


def phase_oracle(qc: QuantumCircuit,
                 control_qubits: Union[QuantumRegister, List[int]],
                 work_qubits: Union[QuantumRegister, List[int]],
                 target_qubit: Union[QuantumRegister, int],
                 state: str
                 ) -> None:
    for i in range(len(state[:-1])):
        if (state[i] == "0"):
            qc.x(control_qubits[i])

    if (state[-1] == "0"):
        qc.x(target_qubit)

    multiple_control_gate(qc, control_qubits, work_qubits, target_qubit)


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
    entries: int = 4

    control: QuantumRegister = QuantumRegister(entries - 1, "ctrl")
    work: QuantumRegister = QuantumRegister(entries - 2, "work")
    target: QuantumRegister = QuantumRegister(1, "target")
    c_bits: ClassicalRegister = ClassicalRegister(entries)
    circuit: QuantumCircuit = QuantumCircuit(control, work, target, c_bits)

    entries = 2**entries
    steps: int = round(acos(1 / sqrt(entries)) / acos((entries - 2) / entries))
    # print(steps)
    # steps = int((pi/4)*sqrt(entries/1))
    # print(steps)

    apply_hadamard_gate(qc=circuit, qubits=control)
    apply_hadamard_gate(qc=circuit, qubits=target)

    for _ in range(steps):
        circuit.barrier()
        phase_oracle(qc=circuit, control_qubits=control,
                     work_qubits=work, target_qubit=target, state="1111")
        circuit.barrier()
        apply_hadamard_gate(qc=circuit, qubits=control)
        apply_hadamard_gate(qc=circuit, qubits=target)

        circuit.barrier()
        apply_z_gate(qc=circuit, qubits=control)
        apply_z_gate(qc=circuit, qubits=target)

        apply_hadamard_gate(qc=circuit, qubits=control)
        apply_hadamard_gate(qc=circuit, qubits=target)

    circuit.measure([control[i] for i in range(len(control))] + [target[0]],
                    [c_bits[i] for i in range(len(c_bits))])

    sim = AerSimulator()
    counts = sim.run(circuit).result().get_counts()

    print(circuit)
    print(counts)


def apply_hadamard_gate(qc: QuantumCircuit,
                        qubits: Union[QuantumRegister, List[int]]
                        ) -> None:
    for qubit in qubits:
        qc.h(qubit)

    return None


def apply_z_gate(qc: QuantumCircuit,
                 qubits: Union[QuantumRegister, List[int]]
                 ) -> None:
    for qubit in qubits:
        qc.z(qubit)

    return None


grover()

# qc = QuantumCircuit(2)
# qc.h(0)
# qc.h(1)
#
# qc.cz(0, 1)
# qc.h(0)
# qc.h(1)
#
# qc.z(0)
# qc.z(1)
# qc.cz(0, 1)
#
# qc.h(0)
# qc.h(1)
#
# qc.measure_all()
#
# sim = AerSimulator()
# counts = sim.run(qc).result().get_counts()
# print(counts)

