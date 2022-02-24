from math import acos, sqrt, pi, ceil
from typing import List

from ket import *


def phase_oracle(qubits: quant, state: str):
    flip_qubits: List = []
    # state = state[::-1]
    for i in range(len(state)):
        if (state[i] == "0"):
            flip_qubits.append(qubits[i])

    if flip_qubits:
        X(flip_qubits)
    ctrl(qubits[:-1], Z, qubits[-1])
    if flip_qubits:
        X(flip_qubits)

    return None


def grover_diffuser(qubits: quant):
    H(qubits)
    X(qubits)

    ctrl(qubits[:-1], Z, qubits[-1])

    X(qubits)
    H(qubits)

    return None


def grover_operator(qubits: quant, states: List[str]):
    for state in states:
        phase_oracle(qubits, state)

    grover_diffuser(qubits)

    return None


def grover(states: List[str]) -> None:
    num_qubits: int = len(states[0])

    qubits: quant = quant(num_qubits)
    entries = 2**num_qubits
    steps: int = int(acos(1 / sqrt(entries)) / acos((entries - 2) / entries))
    # print(steps)
    # steps = int((pi/4)*sqrt(entries/len(states)))
    # print(steps)
    # print(f"Precisão > {(entries - len(states)) / entries}")

    H(qubits)

    for _ in range(steps):
        grover_operator(qubits, states)

    print(dump(qubits).show())

    return None


grover(["1010", "1000", "0101"])
