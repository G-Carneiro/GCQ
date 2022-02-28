from math import sqrt, pi, log2, ceil
from typing import List

from ket import *


def phase_oracle(qubits: quant, state: int):
    ctrl(qubits, Z, qubits[-1], on_state=state)

    return None


def grover_diffuser(qubits: quant):
    H(qubits)

    ctrl(qubits, Z, qubits[-1], on_state=0)

    H(qubits)

    return None


def grover_operator(qubits: quant, states: List[int]):
    for state in states:
        phase_oracle(qubits, state)

    grover_diffuser(qubits)

    return None


def grover(states: List[int]) -> None:
    num_qubits: int = ceil(log2(max(states)))

    qubits: quant = quant(num_qubits)
    entries = 2**num_qubits
    steps = int((pi/4)*sqrt(entries/len(states)))

    H(qubits)

    for _ in range(steps):
        grover_operator(qubits, states)

    print(dump(qubits).show())
    # print(measure(qubits).value)

    return None


grover([10, 8, 5])
