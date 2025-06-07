import sys
from pathlib import Path
import math
from itertools import permutations


lab2_path = str(Path(__file__).parent.parent / "lab2")
sys.path.append(lab2_path)

import functions as f




def to_index_form(snf, number_of_vars):
    index_form, index_subform, i = dict(), [], 0
    while i < len(snf):
        if snf[i] in 'abcde':
            index_subform.append(1)
        if snf[i] == '!' and snf[i + 1] in 'abcde':
            index_subform.append(0)
            i += 1
        if len(index_subform) == number_of_vars:
            index_form[tuple(index_subform)] =  False
            index_subform = []
        i += 1
    return index_form

def can_glue(term1, term2, number_of_vars):
    result = []
    for i in range(number_of_vars):
        if term1[i] == term2[i]:
            result.append(term1[i])
            number_of_vars -= 1
        else:
            result.append('X')
    if number_of_vars == 1:
        return result
    else:
        return []

def glue_terms(index_form, number_of_vars):  #[[1, 1, 0]: True, [1, 0, 0]: False, [0, 1, 0]: True]
    result_keys = list()
    index_form_keys = list(index_form.keys())
    for i in range(len(index_form)):
        term1 = index_form_keys[i]
        j = i + 1
        while j < len(index_form):
            term2 = index_form_keys[j]
            if can_glue(term1, term2, number_of_vars) != [] and tuple(can_glue(term1, term2, number_of_vars)) not in result_keys:
                result_keys.append(tuple(can_glue(term1, term2, number_of_vars))) #[[X, 1, 0]]
                index_form[term1] = True
                index_form[term2] = True
            j += 1
    result = dict.fromkeys(result_keys, False)
    for term in index_form.keys():
        if index_form[term] == False:
            result[term] = False
    return result

def true_table(log_func, vals):
    variables = list()
    repeat_variables = list()
    for i in log_func:
        if i in 'abcde' and i not in variables:
            variables.append(i)
        if i in 'abcde':
            repeat_variables.append(i)
    postf_func = f.transformation(log_func)
    true_table = list()
    for i in range(0, 2**len(variables)):
        table_row = dict.fromkeys(variables)
        values = f.to_binary_system(i, len(variables))
        for j in range(0, len(variables)):
            if variables[j] in vals.keys():
                table_row[variables[j]] = vals[variables[j]]
            else:
                table_row[variables[j]] = values[j]
        values = []
        for j in range(0, len(repeat_variables)):
            values.append(table_row[repeat_variables[j]])
        table_row.update({log_func: f.calculating(postf_func, values)})
        true_table.append(table_row)
    return true_table

def from_index_to_snf(what_snf: str, index_form, vars):
    snf = []
    for term in index_form.keys():
        snf.append('(')
        for i in range(len(term)):
            if term[i] == 1:
                snf.append(vars[i])
                if what_snf == 'sknf':
                    snf.append('|')
                else:
                    snf.append('&')
            elif term[i] == 0:
                snf.append('!')
                snf.append(vars[i])
                if what_snf == 'sknf':
                    snf.append('|')
                else:
                    snf.append('&')
        snf.pop(-1)
        snf.append(')')
        if what_snf == 'sknf':
            snf.append('&')
        else:
            snf.append('|')
    if snf:
        snf.pop(-1)
    return ''.join(map(str, snf))

def glue_snf(what_snf: str, snf, vars):
    glued_snf = ''
    index_form = to_index_form(snf, len(vars))
    for i in range(len(vars) - 1):
        index_form = glue_terms(index_form, len(vars))
        if index_form == {}:
            break
        glued_snf = from_index_to_snf(what_snf, index_form, vars)
    return glued_snf

def calc_is_implicant_extra(what_snf, glued_snf, implicant):
    if what_snf == 'sknf':
        implicants = glued_snf.split('&')
    else:
        implicants = glued_snf.split('|')
    implic = implicant[1:-1]
    if what_snf == 'sknf':
        vars = implic.split('|')
    else:
        vars = implic.split('&')
    values = dict()
    for var in vars:
        if var[0] == '!':
            if what_snf == 'sknf':
                values[var[1]] = 1
            else:
                values[var[1]] = 0
        else:
            if what_snf == 'sknf':
                values[var[0]] = 0
            else:
                values[var[0]] = 1
    other_func = []
    for impl in implicants:
        if impl != implicant:
            other_func.append(impl)
            if what_snf == 'sknf':
                other_func.append('&')
            else:
                other_func.append('|')
    if other_func:
        other_func.pop(-1)
    other_func = ''.join(other_func)
    tr_table = true_table(other_func, values)
    is_extra = False
    for row in tr_table:
        if what_snf == 'sknf':
            if row[other_func] == 0:
                is_extra = True
            else:
                is_extra = False
                break
        else:
            if row[other_func] == 1:
                is_extra = True
            else:
                is_extra = False
                break
    if is_extra:
        return True
    else:
        return False

def delete_subsnf(snf, subsnf):
    index = snf.index(subsnf)
    if index == 0:
        return snf[len(subsnf) + 1:]
    if index + len(subsnf) == len(snf):
        return snf[:index - 1]
    else:
        return snf[:index - 1] + snf[index + len(subsnf):]

def calc_check_implic_snf(what_snf: str, glued_snf, implicants):
    if len(implicants) == 1:
        return [], implicants
    extra_implicants = list()
    new_glued_snf = glued_snf[:]
    for i in range(len(implicants)):
        if calc_is_implicant_extra(what_snf, new_glued_snf, implicants[i]):
            new_glued_snf = delete_subsnf(new_glued_snf, implicants[i])
            extra_implicants.append(implicants[i])
    return extra_implicants

def create_minim_table(what_snf, snf, glued_snf):
    if what_snf == 'sknf':
        constituents = snf.split('&')
        implicants = glued_snf.split('&')
    else:
        constituents = snf.split('|')
        implicants = glued_snf.split('|')
    table = list()
    for i in range(len(implicants)):
        implics = implicants[i][1:-1]
        if what_snf == 'sknf':
            impl_vars = implics.split('|')
        else:
            impl_vars = implics.split('&')
        row = list()
        for j in range(len(constituents)):
            consts = constituents[j][1:-1]
            if what_snf == 'sknf':
                const_vars = consts.split('|')
            else:
                const_vars = consts.split('&')
            if all(var in const_vars for var in impl_vars):
                row.append('X')
            else:
                row.append(' ')
        table.append(row)
    return table, constituents, implicants

def is_implicant_extra(all_const_X, implic_X):
    new_const_X = all_const_X[:]
    for i in range(len(implic_X)):
        new_const_X[i] -= implic_X[i]
    if all(number_of_X > 0 for number_of_X in new_const_X):
        return True
    else:
        return False

def calc_table_is_implicant_extra(table, impl_index):
    all_const_X = [0 for _ in range(len(table[0]))]
    for i in range(len(table[0])):
        for j in range(len(table)):
            if table[j][i] == 'X':
                all_const_X[i] += 1
    implic_X = [0 for _ in range(len(table[impl_index]))]
    for i in range(len(table[impl_index])):
        if table[impl_index][i] == 'X':
            implic_X[i] += 1
    if is_implicant_extra(all_const_X, implic_X):
        return True
    else:
        return False

def calc_table_check_implic_snf(table, implicants):
    new_table = table[:]
    extra_implicants = list()
    index = 0
    for i in range(len(implicants)):
        if calc_table_is_implicant_extra(new_table, index):
            new_table.pop(index)
            extra_implicants.append(implicants[i])
        else:
            index += 1
    return extra_implicants

def print_implicant_table(table, constituents, implicants):
    col_widths = [12] + [max(len(c), 3) for c in constituents]
    header = ["Импликанты"] + constituents
    print(" | ".join(f"{cell:^{width}}" for cell, width in zip(header, col_widths)))
    for i, implicant in enumerate(implicants):
        row = [implicant] + table[i]
        print(" | ".join(f"{cell:^{width}}" for cell, width in zip(row, col_widths)))

def to_Grey_code(decimal_number, bit_depth):
    binary_number = f.to_binary_system(decimal_number, bit_depth)
    Grey_code = str(binary_number[0])
    for i in range(1, len(binary_number)):
        number = 0
        for j in range(0, i):
            if Grey_code[j] == '1':
                number += 1
        if number % 2 == 0:
            Grey_code += str(binary_number[i])
        else:
            Grey_code += str(int(not binary_number[i]))
    return Grey_code

def print_map_karno(map_karno, hor_values, vert_values, vars):
    n = len(vars)
    num_vert_bits = len(vert_values[0])
    vert_vars = vars[:num_vert_bits]
    hor_vars = vars[num_vert_bits:]
    vert_header = ''.join(vert_vars)
    hor_header = ''.join(hor_vars)
    header = f"{vert_header} \\ {hor_header}"
    print(f"{header:>7}", end=" | ")
    print(" | ".join(hor_values))
    print("-" * (8 + len(hor_values) * 5))
    for i, row in enumerate(map_karno):
        print(f"{vert_values[i]:>7}", end=" | ")
        print(" | ".join(map(str, row)))
        print("-" * (8 + len(hor_values) * 5))

def constituent_to_values(what_snf, const):
    values = ''
    if what_snf == 'sknf':
        vars = const[1:].split('|')
        for var in vars:
            if var[0] == '!':
                values += '1'
            else:
                values += '0'
    if what_snf == 'sdnf':
        vars = const[1:].split('&')
        for var in vars:
            if var[0] == '!':
                values += '0'
            else:
                values += '1'
    return values

def create_map_karno(what_snf, snf, n):
    num_vert_bits = n // 2
    num_hor_bits = n - num_vert_bits
    map_karno = [[-1 for _ in range(2 ** num_hor_bits)] for _ in range(2 ** num_vert_bits)]
    horizontal_values, vertical_values = list(), list()
    for i in range(2 ** n):
        Grey_code = to_Grey_code(i, n)
        vert = Grey_code[:num_vert_bits]
        hor = Grey_code[num_vert_bits:]
        if hor not in horizontal_values:
            horizontal_values.append(hor)
        if vert not in vertical_values:
            vertical_values.append(vert)
    constituents = []
    if what_snf == 'sknf':
        constituents = snf.split('&')
    if what_snf == 'sdnf':
        constituents = snf.split('|')
    for const in constituents:
        values = constituent_to_values(what_snf, const)
        for i in range(len(vertical_values)):
            for j in range(len(horizontal_values)):
                if values == vertical_values[i] + horizontal_values[j]:
                    if what_snf == 'sknf':
                        map_karno[i][j] = 0
                    if what_snf == 'sdnf':
                        map_karno[i][j] = 1
    for i in range(len(map_karno)):
        for j in range(len(map_karno[i])):
            if map_karno[i][j] == -1:
                if what_snf == 'sknf':
                    map_karno[i][j] = 1
                if what_snf == 'sdnf':
                    map_karno[i][j] = 0
    return map_karno, horizontal_values, vertical_values

def find_groups(map_karno, what_snf):
    rows, cols = len(map_karno), len(map_karno[0])
    target = 1 if what_snf == 'sdnf' else 0
    all_groups = []

    def is_valid_group(r, c, h, w):
        for i in range(h):
            for j in range(w):
                ri = (r + i) % rows
                cj = (c + j) % cols
                if map_karno[ri][cj] != target:
                    return False
        return True

    # генерируем все возможные группы
    pow2_heights = [2 ** i for i in range(int(math.log2(rows)) + 1)][::-1]
    pow2_widths = [2 ** i for i in range(int(math.log2(cols)) + 1)][::-1]
    for h in pow2_heights:
        for w in pow2_widths:
            for r in range(rows):
                for c in range(cols):
                    if is_valid_group(r, c, h, w):
                        all_groups.append((r, c, h, w))

    # сортировка: большие группы — приоритетнее
    all_groups.sort(key=lambda g: -(g[2] * g[3]))

    used = [[False] * cols for _ in range(rows)]
    final_groups = []

    def group_cells(g):
        r, c, h, w = g
        return {( (r + i) % rows, (c + j) % cols ) for i in range(h) for j in range(w)}

    # выбираем непересекающиеся группы
    covered = set()
    for g in all_groups:
        cells = group_cells(g)
        if not cells & covered:
            final_groups.append(g)
            covered |= cells

    return final_groups



def table_find_implic_snf(what_snf, map_karno, hor_values, vert_values, vars):
    implics = list()
    rectangles = find_groups(map_karno, what_snf)
    num_vert_bits = len(vert_values[0])
    vert_vars = vars[:num_vert_bits]
    hor_vars = vars[num_vert_bits:]
    for rect in rectangles:
        var_values = {var: [] for var in vars}
        implic = '('
        for i in range(rect[0], rect[0] + rect[2]):
            for x in range(len(vert_vars)):
                var_values[vert_vars[x]].append(vert_values[i % len(vert_values)][x])
            for j in range(rect[1], rect[1] + rect[3]):
                for x in range(len(hor_vars)):
                    var_values[hor_vars[x]].append(hor_values[j % len(hor_values)][x])
        for var in var_values.keys():
            if all(value == '0' for value in var_values[var]) or \
               all(value == '1' for value in var_values[var]):
                if what_snf == 'sknf':
                    implic += f'{var}|' if var_values[var][0] == '0' else f'!{var}|'
                if what_snf == 'sdnf':
                    implic += f'{var}&' if var_values[var][0] == '1' else f'!{var}&'
        implic = implic[:-1]
        implic += ')'
        implics.append(implic)
    return implics

def find_minim_snf_from_all_snf(all_snf):
    keys = list(all_snf.keys())
    min = all_snf[keys[0]]
    minim_snf = keys[0]
    for key in keys:
        if all_snf[key] < min:
            min = all_snf[key]
            minim_snf = key
    return minim_snf

def create_new_table(table, implicants, new_implicants):
    new_table = []
    for i in range(len(implicants)):
        index = implicants.index(new_implicants[i])
        new_table.append(table[index])
    return new_table


def calc_minim_snf(what_snf, snf):
    if what_snf == 'sknf':
        implicants = snf.split('&')
    if what_snf == 'sdnf':
        implicants = snf.split('|')
    all_implicants = [list(p) for p in permutations(implicants)]
    all_minim_snf = {}
    for i in range(len(all_implicants)):
        implicants = all_implicants[i]
        extra_implicants = calc_check_implic_snf(what_snf, snf, implicants)
        minim_snf = ''
        for implicant in implicants:
            if implicant not in extra_implicants:
                minim_snf += implicant
                if what_snf == 'sknf':
                    minim_snf += '&'
                else:
                    minim_snf += '|'
        minim_snf = minim_snf[:-1]
        if what_snf == 'sknf':
            impls = minim_snf.split('&')
        if what_snf == 'sdnf':
            impls = minim_snf.split('|')
        all_minim_snf[minim_snf] = len(impls)
    return find_minim_snf_from_all_snf(all_minim_snf)



def calc_table_minim_snf(what_snf, table, implicants):
    all_implicants = [list(p) for p in permutations(implicants)]
    all_minim_snf = {}
    for i in range(len(all_implicants)):
        new_implicants = all_implicants[i]
        new_table = create_new_table(table, implicants, new_implicants)
        extra_implicants = calc_table_check_implic_snf(new_table, new_implicants)
        minim_snf = ''
        for implicant in new_implicants:
            if implicant not in extra_implicants:
                minim_snf += implicant
                if what_snf == 'sknf':
                    minim_snf += '&'
                else:
                    minim_snf += '|'
        minim_snf = minim_snf[:-1]
        if what_snf == 'sknf':
            impls = minim_snf.split('&')
        if what_snf == 'sdnf':
            impls = minim_snf.split('|')
        all_minim_snf[minim_snf] = len(impls)
    return find_minim_snf_from_all_snf(all_minim_snf)

def table_minim_snf(what_snf, map_karno, hor_values, vert_values, vars):
    implicants = table_find_implic_snf(what_snf, map_karno, hor_values, vert_values, vars)
    minim_snf = ''
    for implicant in implicants:
        minim_snf += implicant
        if what_snf == 'sknf':
            minim_snf += '&'
        if what_snf == 'sdnf':
            minim_snf += '|'
    if minim_snf:
        minim_snf = minim_snf[:-1]
    return minim_snf