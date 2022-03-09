from time import time
from typing import List, Tuple
from tabulate import tabulate

from grover import grover
from grover_ket import grover as gk

print(tabulate([[0, 1], [0, 1]], headers=["zero", "um"], tablefmt="plain", numalign="left"))
# qubits, quantidade de aplicação de G, precisão, tempo, nº de estados desejados
# ket-local, ket-qubox, Aer, IBMQ

states: List[int] = [0]
replications: int = 1000

headers: List[str] = ["qubits", "states", "replications", "total time", "precision"]
num_states: int = len(states)
table: List[Tuple[int, int, int, float, float]] = []

for num_qubits in range(2, 31):
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
    new_entry = (num_qubits, num_states, replications, average_total_time, precision)
    table.append(new_entry)
