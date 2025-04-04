import functions as f

log_func = input()
true_table, variables = f.build_true_table(log_func)
print('Таблица истинности:')
headers = list(true_table[0].keys())
column_widths = [
    max(len(str(row[h])) for row in true_table)
    if h in true_table[0] else len(h)
    for h in headers
]
print("".join(h.ljust(w + 2) for h, w in zip(headers, column_widths)))
for row in true_table:
    print("".join(str(row[h]).ljust(w + 2) for h, w in zip(headers, column_widths)))
print('СДНФ: ', f.build_sdnf(true_table, log_func, variables))
print('СКНФ: ', f.build_sknf(true_table, log_func, variables))
print('Числовая форма для СДНФ: ', f.build_numeric_form_sdnf(true_table, log_func, variables))
print('Числовая форма для СДНФ: ', f.build_numeric_form_sknf(true_table, log_func, variables))
print('Индексная форма функции: ', f.build_index_form(true_table, log_func))
