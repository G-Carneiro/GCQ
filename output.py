from time import time
from typing import List, Tuple
from random import randint

from tabulate import tabulate

from grover_ket import grover


replications: int = 100

headers: List[str] = ["qubits", "states", "replications", "total time", "precision"]
table: List[Tuple[int, int, int, float, float]] = []

for num_qubits in range(2, 20):
    print(num_qubits)
    founded_state: int = 0
    sum_total_time: float = 0
    num_states: int = 1
    for _ in range(replications):
        states: List[int] = []
        while (num_states > len(states)):
            new_state: int = randint(0, 2**num_states - 1)
            if new_state not in states:
                states.append(new_state)

        start: float = time()
        result_state: int = grover(states, num_qubits)
        sum_total_time += time() - start
        if (result_state in states):
            founded_state += 1

    average_total_time: float = sum_total_time / replications
    precision: float = founded_state / replications
    new_entry = (num_qubits, num_states, replications, average_total_time, precision)
    table.append(new_entry)

with open("ket_qubox_pbwd_01.dat", "w") as file:
    file.write(tabulate(table, headers=["qubits", "states", "replications", "average", "precision"],
                        tablefmt="plain", numalign="left"))
