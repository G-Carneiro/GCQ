from math import sqrt, pi
from typing import List

from ket import *
from quantuloop import qubox_ufsc

from src.utils.utils import qubox_token

qubox_ufsc.set_token(qubox_token)
qubox_ufsc.set_backend("pbwd")


def phase_oracle(qubits: quant, state: int) -> None:
    ctrl(qubits, Z, qubits[-1], on_state=state)

    return None


def grover_diffuser(qubits: quant):
    H(qubits)

    ctrl(qubits, Z, qubits[-1], on_state=0)

    H(qubits)

    return None


def grover_operator(qubits: quant, states: List[int]) -> None:
    for state in states:
        phase_oracle(qubits, state)

    grover_diffuser(qubits)

    return None


def grover(states: List[int], num_qubits: int) -> int:
    qubits: quant = quant(num_qubits)
    entries = 2**num_qubits
    steps = int((pi/4)*sqrt(entries/len(states)))

    H(qubits)

    for _ in range(steps):
        grover_operator(qubits, states)

    return measure(qubits).value
