from functions import *

table = HashTable()
while True:
    print('1. Просмотр таблицы')
    print('2. Добавление строки в таблицу')
    print('3. Поиск в таблице по ключу')
    print('4. Удаление строки из таблицы по ключу')
    print('5. Выход')
    choise = int(input('Выберите действие(введите число): '))
    match choise:
        case 1:
            table.print_pretty_table()
        case 2:
            while True:
                key = input('Введите ключ(ID)(ключ должен состоять только из русских букв): ')
                if key in table._keys:
                    print('Такой ключ уже есть!')
                    continue
                data = input('Введите данные: ')
                row = TableRow(key, data)
                if hasattr(row, '_id') == 0:
                    continue
                table.add_row(row)
                break
        case 3:
            key = input('Введите ключ(ID): ')
            row = table.get_row(key)
            if row != None:
                print(f'ключ: {row._id} \n' 
                      f'числовое значение: {row._value} \n'
                      f'хеш: {row._hash} \n'
                      f'данные: {row._data} \n'
                      f'U: {row._U_flag} \n'
                      f'C: {row._C_flag} \n'
                      f'T: {row._T_flag} \n'
                      f'L: {row._L_flag} \n'
                      f'D: {row._D_flag} \n'
                      f'P0: {row._P0} \n')
        case 4:
            key = input('Введите ключ(ID): ')
            table.delete_row(key)
        case 5:
            break
        case _:
            print('Введено число не от 1 до 5!')

