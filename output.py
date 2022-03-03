from time import time
from typing import List

from grover import grover
from grover_ket import grover as gk


# qubits, quantidade de aplicação de G, precisão, tempo, nº de estados desejados
# ket-local, ket-qubox, Aer, IBMQ

states: List[int] = [0]
replications: int = 1000

for num_qubits in range(2, 31):
    for run in ["ket-local", "ket-qubox", "Aer", "IBMQ"]:
        founded_state: int = 0
        sum_total_time: float = 0
        for _ in range(replications):
            start: float = time()
            result_state: int = grover(states)
            sum_total_time += time() - start
            if (result_state in states):
                founded_state += 1

        average_total_time: float = sum_total_time / replications
        precision: float = founded_state / replications
