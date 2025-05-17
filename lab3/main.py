import sys
from pathlib import Path

from lab3_functions import delete_subsnf

lab2_path = str(Path(__file__).parent.parent / "lab2")
sys.path.append(lab2_path)

import functions as l2f

import lab3_functions as f

if __name__ == "__main__":
    while True:
        print('1. Минимизация СКНФ расчетным методом')
        print('2. Минимизация СДНФ расчетным методом')
        print('3. Минимизация СКНФ расчетно-табличным методом')
        print('4. Минимизация СДНФ расчетно-табличным методом')
        print('5. Минимизация СКНФ табличным методом')
        print('6. Минимизация СДНФ табличным методом')
        print('7. Выход')
        choise = int(input('Выберите действие: '))
        match choise:
            case 1:
                log_func = input('Введите логическую функцию: ')
                table, vars = l2f.build_true_table(log_func)
                sknf = l2f.build_sknf(table, log_func, vars)
                print(f'СКНФ: {sknf}')
                calc_minim_sknf = f.calc_minim_snf('sknf', sknf, vars)
                print(f'Минимизированная СКНФ: {calc_minim_sknf}')
            case 2:
                log_func = input('Введите логическую функцию: ')
                table, vars = l2f.build_true_table(log_func)
                sdnf = l2f.build_sdnf(table, log_func, vars)
                print(f'СДНФ: {sdnf}')
                calc_minim_sdnf = f.calc_minim_snf('sdnf', sdnf, vars)
                print(f'Минимизированная СДНФ: {calc_minim_sdnf}')
            case 3:
                log_func = input('Введите логическую функцию: ')
                table, vars = l2f.build_true_table(log_func)
                sknf = l2f.build_sknf(table, log_func, vars)
                print(f'СКНФ: {sknf}')
                calc_table_minim_sknf = f.calc_table_minim_snf('sknf', sknf, vars)
                print(f'Минимизированная СКНФ: {calc_table_minim_sknf}')
            case 4:
                log_func = input('Введите логическую функцию: ')
                table, vars = l2f.build_true_table(log_func)
                sdnf = l2f.build_sdnf(table, log_func, vars)
                print(f'СДНФ: {sdnf}')
                calc_table_minim_sdnf = f.calc_table_minim_snf('sdnf', sdnf, vars)
                print(f'Минимизированная СДНФ: {calc_table_minim_sdnf}')
            case 5:
                log_func = input('Введите логическую функцию: ')
                table, vars = l2f.build_true_table(log_func)
                sknf = l2f.build_sknf(table, log_func, vars)
                print(f'СКНФ: {sknf}')
                table_minim_sknf = f.table_minim_snf('sknf', sknf, vars)
                print(f'Минимизированная СКНФ: {table_minim_sknf}')
            case 6:
                log_func = input('Введите логическую функцию: ')
                table, vars = l2f.build_true_table(log_func)
                sdnf = l2f.build_sdnf(table, log_func, vars)
                print(f'СДНФ: {sdnf}')
                table_minim_sdnf = f.table_minim_snf('sdnf', sdnf, vars)
                print(f'Минимизированная СДНФ: {table_minim_sdnf}')
            case 7:
                break
            case _:
                print('Введено число не от 1 до 7!')




