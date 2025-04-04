def prior(a):
    match (a):
        case '!':
            return 3
        case '&'| '|' | '>' | '~':
            return 2
        case '(':
            return 1
    return 0

def transformation(inf_expression: str):
    stack = list()
    postf_expression = list()
    a = ' '
    for i in range(0, len(inf_expression)):
        if inf_expression[i] == '(':
            stack.append(inf_expression[i])
        if inf_expression[i] == ')':
            while stack[len(stack)-1] != '(':
                a = stack.pop()
                postf_expression.append(a)
            a = stack.pop()
        if inf_expression[i] in 'abcde':
            postf_expression.append(inf_expression[i])
        if inf_expression[i] in '!&|>~':
            while stack != [] and prior(stack[len(stack)-1]) >= prior(inf_expression[i]):
                a = stack.pop()
                postf_expression.append(a)
            stack.append(inf_expression[i])
    while stack != []:
        a = stack.pop()
        postf_expression.append(a)
    return postf_expression



def calculating(postf_expression: list, values: list):
    z = 0
    stack = list()
    result = None
    for i in range(0, len(postf_expression)):
        if postf_expression[i] in 'abcde':
            stack.append(values[z])
            z += 1
        elif postf_expression[i] == '!':
            value = stack.pop()
            result = int(not value)
            stack.append(result)
        else:
            value1 = stack.pop()
            value2 = stack.pop()
            match postf_expression[i]:
                case '&':
                    result = int(value2 and value1)
                case '|':
                    result = int(value2 or value1)
                case '>':
                    result = int(not value2 or value1)
                case '~':
                    result = int(value2 == value1)
            stack.append(result)
    return result

def to_binary_system(decimal_number, bit_depth):
    quotient = abs(decimal_number)
    binary_number = list()
    while quotient >= 2:
        binary_number.insert(0, quotient % 2)
        quotient = quotient // 2
    binary_number.insert(0, quotient)
    while len(binary_number) != bit_depth:
        binary_number.insert(0, 0)
    return binary_number

def to_decimal_system(bin_num: list):
    bit_depth = len(bin_num) - 1
    result = 0
    for i in range(0, len(bin_num)):
        result += bin_num[i] * 2**bit_depth
        bit_depth -= 1
    return result

def build_true_table(log_func):
    variables = list()
    repeat_variables = list()
    for i in log_func:
        if i in 'abcde' and i not in variables:
            variables.append(i)
        if i in 'abcde':
            repeat_variables.append(i)
    postf_func = transformation(log_func)
    true_table = list()
    for i in range(0, 2**len(variables)):
        table_row = dict.fromkeys(variables)
        values = to_binary_system(i, len(variables))
        for j in range(0, len(variables)):
            table_row[variables[j]] = values[j]
        values = []
        for j in range(0, len(repeat_variables)):
            values.append(table_row[repeat_variables[j]])
        table_row.update({log_func: calculating(postf_func, values)})
        true_table.append(table_row)
    return true_table, variables

def build_sknf(true_table, result: str, vars):
    sknf = list()
    for row in true_table:
        if row[result] == 0:
            sknf.append('(')
            i = 0
            while i < len(vars):
                if row[vars[i]] == 0:
                    sknf.append(str(vars[i]))
                else:
                    sknf.append('!')
                    sknf.append(str(vars[i]))
                if i != len(vars) - 1:
                    sknf.append('|')
                i += 1
            sknf.append(')')
            sknf.append('&')
    if sknf:
        sknf.pop(-1)
    return ''.join(sknf)

def build_sdnf(true_table, result: str, vars):
    sdnf = list()
    for row in true_table:
        if row[result] == 1:
            sdnf.append('(')
            i = 0
            while i < len(vars):
                if row[vars[i]] == 1:
                    sdnf.append(str(vars[i]))
                else:
                    sdnf.append('!')
                    sdnf.append(str(vars[i]))
                if i != len(vars) - 1:
                    sdnf.append('&')
                i += 1
            sdnf.append(')')
            sdnf.append('|')
    if sdnf:
        sdnf.pop(-1)
    return ''.join(sdnf)

def build_numeric_form_sknf(true_table, result: str, vars):
    num_form = ['(']
    for row in true_table:
        if row[result] == 0:
            num = list()
            i = 0
            while i < len(vars):
                num.append(row[vars[i]])
                i += 1
            num_form.append(to_decimal_system(num))
            num_form.append(', ')
    if num_form[-1] == ', ':
        num_form.pop(-1)
    num_form.append(')')
    num_form.append(' &')
    return ''.join(map(str, num_form))

def build_numeric_form_sdnf(true_table, result: str, vars):
    num_form = ['(']
    for row in true_table:
        if row[result] == 1:
            num = list()
            i = 0
            while i < len(vars):
                num.append(row[vars[i]])
                i += 1
            num_form.append(to_decimal_system(num))
            num_form.append(', ')
    if num_form[-1] == ', ':
        num_form.pop(-1)
    num_form.append(')')
    num_form.append(' |')
    return ''.join(map(str, num_form))

def build_index_form(true_table, result):
    index_form = list()
    for row in true_table:
        index_form.append(row[result])
    index = to_decimal_system(index_form)
    return str(index) + ' - ' + ''.join(map(str, index_form))
