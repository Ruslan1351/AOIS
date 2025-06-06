import sys
from pathlib import Path

lab2_path = str(Path(__file__).parent.parent / "lab2")
sys.path.append(lab2_path)
lab3_path = str(Path(__file__).parent.parent / "lab3")
sys.path.append(lab3_path)

import functions as l2f
import lab3_functions as l3f

def print_table(table):
    headers = table[0].keys()
    column_widths = [
        max(len(str(row[h])) for row in table)
        if h in table[0] else len(h)
        for h in headers
    ]
    print("".join(h.ljust(w + 2) for h, w in zip(headers, column_widths)))
    for row in table:
        print("".join(str(row[h]).ljust(w + 2) for h, w in zip(headers, column_widths)))

def change_sdnf(sdnf):
    new_sdnf = sdnf.replace('a', '(q3*)')
    new_sdnf = new_sdnf.replace('b', '(q2*)')
    new_sdnf = new_sdnf.replace('c', '(q1*)')
    new_sdnf = new_sdnf.replace('d', 'V')
    return new_sdnf

def get_true_table(table, results):
    for i in range(len(results)):
        table[i]['h'] = results[i]
    return table


transition_true_table = [{'q3*': 1, 'q2*': 1, 'q1*': 1, 'V': 1, 'q3': 1, 'q2': 1, 'q1': 0},
                         {'q3*': 1, 'q2*': 1, 'q1*': 1, 'V': 0, 'q3': 1, 'q2': 1, 'q1': 1},
                         {'q3*': 1, 'q2*': 1, 'q1*': 0, 'V': 1, 'q3': 1, 'q2': 0, 'q1': 1},
                         {'q3*': 1, 'q2*': 1, 'q1*': 0, 'V': 0, 'q3': 1, 'q2': 1, 'q1': 0},
                         {'q3*': 1, 'q2*': 0, 'q1*': 1, 'V': 1, 'q3': 1, 'q2': 0, 'q1': 0},
                         {'q3*': 1, 'q2*': 0, 'q1*': 1, 'V': 0, 'q3': 1, 'q2': 0, 'q1': 1},
                         {'q3*': 1, 'q2*': 0, 'q1*': 0, 'V': 1, 'q3': 0, 'q2': 1, 'q1': 1},
                         {'q3*': 1, 'q2*': 0, 'q1*': 0, 'V': 0, 'q3': 1, 'q2': 0, 'q1': 0},
                         {'q3*': 0, 'q2*': 1, 'q1*': 1, 'V': 1, 'q3': 0, 'q2': 1, 'q1': 0},
                         {'q3*': 0, 'q2*': 1, 'q1*': 1, 'V': 0, 'q3': 0, 'q2': 1, 'q1': 1},
                         {'q3*': 0, 'q2*': 1, 'q1*': 0, 'V': 1, 'q3': 0, 'q2': 0, 'q1': 1},
                         {'q3*': 0, 'q2*': 1, 'q1*': 0, 'V': 0, 'q3': 0, 'q2': 1, 'q1': 0},
                         {'q3*': 0, 'q2*': 0, 'q1*': 1, 'V': 1, 'q3': 0, 'q2': 0, 'q1': 0},
                         {'q3*': 0, 'q2*': 0, 'q1*': 1, 'V': 0, 'q3': 0, 'q2': 0, 'q1': 1},
                         {'q3*': 0, 'q2*': 0, 'q1*': 0, 'V': 1, 'q3': 1, 'q2': 1, 'q1': 1},
                         {'q3*': 0, 'q2*': 0, 'q1*': 0, 'V': 0, 'q3': 0, 'q2': 0, 'q1': 0}]
print(f'Таблица переходов двоичного вычитающего счетчика:')
print_table(transition_true_table)

trigger_true_table = [{'a': 1, 'b': 1, 'c': 1, 'd': 1, 'h': 0},
                      {'a': 1, 'b': 1, 'c': 1, 'd': 0, 'h': 0},
                      {'a': 1, 'b': 1, 'c': 0, 'd': 1, 'h': 0},
                      {'a': 1, 'b': 1, 'c': 0, 'd': 0, 'h': 0},
                      {'a': 1, 'b': 0, 'c': 1, 'd': 1, 'h': 0},
                      {'a': 1, 'b': 0, 'c': 1, 'd': 0, 'h': 0},
                      {'a': 1, 'b': 0, 'c': 0, 'd': 1, 'h': 0},
                      {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'h': 0},
                      {'a': 0, 'b': 1, 'c': 1, 'd': 1, 'h': 0},
                      {'a': 0, 'b': 1, 'c': 1, 'd': 0, 'h': 0},
                      {'a': 0, 'b': 1, 'c': 0, 'd': 1, 'h': 0},
                      {'a': 0, 'b': 1, 'c': 0, 'd': 0, 'h': 0},
                      {'a': 0, 'b': 0, 'c': 1, 'd': 1, 'h': 0},
                      {'a': 0, 'b': 0, 'c': 1, 'd': 0, 'h': 0},
                      {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'h': 0},
                      {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'h': 0}]

results = [[0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0],
           [0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
           [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]]

for i in range(len(results)):
    true_table = get_true_table(trigger_true_table, results[i])
    sdnf = l2f.build_sdnf(true_table, 'h', ['a', 'b', 'c', 'd'])
    map_karno, hor_values, vert_values = l3f.create_map_karno('sdnf', sdnf, 4)
    minim_sdnf = l3f.table_minim_snf('sdnf', map_karno, hor_values, vert_values, ['a', 'b', 'c', 'd'])
    print(f'ТДНФ для h{len(results) - i}: {change_sdnf(minim_sdnf)}')