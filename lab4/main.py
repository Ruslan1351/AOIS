import sys
from pathlib import Path

lab2_path = str(Path(__file__).parent.parent / "lab2")
sys.path.append(lab2_path)
lab3_path = str(Path(__file__).parent.parent / "lab3")
sys.path.append(lab3_path)

import functions as l2f
import lab3_functions as l3f

def print_table(table):
    headers = list(table[0].keys())
    column_widths = [
        max(len(str(row[h])) for row in table)
        if h in table[0] else len(h)
        for h in headers
    ]
    print("".join(h.ljust(w + 2) for h, w in zip(headers, column_widths)))
    for row in table:
        print("".join(str(row[h]).ljust(w + 2) for h, w in zip(headers, column_widths)))

def inverse_sdnf(sdnf):
    inversed_sdnf = sdnf[:]
    length, i = len(inversed_sdnf), 0
    while i < length:
        if inversed_sdnf[i] == '!':
            inversed_sdnf = inversed_sdnf[:i] + inversed_sdnf[i+1:]
            length -= 1
            i += 1
        if inversed_sdnf[i] in 'abcde':
            inversed_sdnf = inversed_sdnf[0:i] + '!' + inversed_sdnf[i:]
            length += 1
            i += 1
        i += 1
    return inversed_sdnf


def get_true_table(table, results):
    for i in range(len(results)):
        table[i]['res'] = results[i]
    return table


summator_true_table = [{'a': 0,'b': 0, 'c': 0,'P': 0, 'S': 0},
                       {'a': 0,'b': 0, 'c': 1,'P': 0, 'S': 1},
                       {'a': 0,'b': 1, 'c': 0,'P': 0, 'S': 1},
                       {'a': 0,'b': 1, 'c': 1,'P': 1, 'S': 0},
                       {'a': 1,'b': 0, 'c': 0,'P': 0, 'S': 1},
                       {'a': 1,'b': 0, 'c': 1,'P': 1, 'S': 0},
                       {'a': 1,'b': 1, 'c': 0,'P': 1, 'S': 0},
                       {'a': 1,'b': 1, 'c': 1,'P': 1, 'S': 1}]
vars = ['a', 'b', 'c']
print('Таблица истинности:')
print_table(summator_true_table)

P_sdnf = l2f.build_sdnf(summator_true_table, 'P', vars)
S_sdnf = l2f.build_sdnf(summator_true_table, 'S', vars)
print(f'P(СДНФ): {P_sdnf}')
print(f'S(СДНФ): {S_sdnf}')

inv_P_sdnf = inverse_sdnf(P_sdnf)
print(f'!P(СДНФ): {inv_P_sdnf}')

print('!P(СДНФ) и S(СДНФ) совпадают по 3 конституэнтам(!a&!b&c, !a&b&!c, a&!b&!c) => _P = !P - (!a&!b&!c) = !P&(a|b|c) - общая часть S и !P')
print('То есть, выходная формула суммы S(ТДНФ) = _P|(a&b&c) = !P&(a|b|c)|(a&b&c), где P - P(ТДНФ) - минимизированная функция переноса')

map_karno, hor_values, vert_values = l3f.create_map_karno('sdnf', P_sdnf, len(vars))
minim_P_sdnf = l3f.table_minim_snf('sdnf', map_karno, hor_values, vert_values, vars)
print(f'P(ТДНФ): {minim_P_sdnf}')
map_karno, hor_values, vert_values = l3f.create_map_karno('sdnf', S_sdnf, len(vars))
minim_S_sdnf = l3f.table_minim_snf('sdnf', map_karno, hor_values, vert_values, vars)
print(f'S(ТДНФ): {minim_S_sdnf}')

print()

d8421_true_table = [{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'res': 0},
                     {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'res': 0},
                     {'a': 0, 'b': 0, 'c': 1, 'd': 0, 'res': 0},
                     {'a': 0, 'b': 0, 'c': 1, 'd': 1, 'res': 0},
                     {'a': 0, 'b': 1, 'c': 0, 'd': 0, 'res': 0},
                     {'a': 0, 'b': 1, 'c': 0, 'd': 1, 'res': 0},
                     {'a': 0, 'b': 1, 'c': 1, 'd': 0, 'res': 0},
                     {'a': 0, 'b': 1, 'c': 1, 'd': 1, 'res': 0},
                     {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'res': 0},
                     {'a': 1, 'b': 0, 'c': 0, 'd': 1, 'res': 0},
                     {'a': 1, 'b': 0, 'c': 1, 'd': 0, 'res': 0},
                     {'a': 1, 'b': 0, 'c': 1, 'd': 1, 'res': 0},
                     {'a': 1, 'b': 1, 'c': 0, 'd': 0, 'res': 0},
                     {'a': 1, 'b': 1, 'c': 0, 'd': 1, 'res': 0},
                     {'a': 1, 'b': 1, 'c': 1, 'd': 0, 'res': 0},
                     {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'res': 0}]


results = [[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
           [0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1],
           [0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,1],
           [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]]

for i in range(len(results)):
    true_table = get_true_table(d8421_true_table, results[i])
    sdnf = l2f.build_sdnf(true_table, 'res', ['a', 'b', 'c', 'd'])
    map_karno, hor_values, vert_values = l3f.create_map_karno('sdnf', sdnf, 4)
    minim_sdnf = l3f.table_minim_snf('sdnf', map_karno, hor_values, vert_values, ['a', 'b', 'c', 'd'])
    print(f'ТДНФ для {i+1}-го бита: {minim_sdnf}')

