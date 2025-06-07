from functions import *

size = int(input('Введите размер матрицы: '))
m = DiagonalMatrix(size)

while True:
    print('1. Добавить слово')
    print('2. Получить слово')
    print('3. Добавить разрядный столбец')
    print('4. Получить разрядный столбец')
    print('5. Выполнить логические операции над словами')
    print('6. Выполнить логические операции над разрядными столбцами')
    print('7. Найти ближайшее значение снизу')
    print('8. Найти ближайшее значение сверху')
    print('9. Найти сумму полей')
    print('10. Вывод матрицы')
    print('11. Выход')
    choise = int(input('Выберите действие(введите число): '))
    match choise:
        case 1:
            word = input('Введите слово(размером в длину матрицы): ')
            i = int(input('Введите индекс строки для вставки: '))
            j = int(input('Введите индекс столбца для вставки: '))
            m.set_word(i, j, [int(word[i]) for i in range(len(word))])
        case 2:
            i = int(input('Введите индекс столбца: '))
            print(m.get_word(i))
        case 3:
            column = input('Введите разрядный столбец(размером в длину матрицы): ')
            i = int(input('Введите индекс для вставки: '))
            m.set_column(i, [int(column[i]) for i in range(len(column))])
        case 4:
            i = int(input('Введите индекс разрядного столбца: '))
            print(m.get_column(i))
        case 5:
            i1 = int(input('Введите индекс столбца первого слова: '))
            word1 = m.get_word(i1)
            i2 = int(input('Введите индекс столбца второго слова: '))
            word2 = m.get_word(i2)
            print(f'Первое слово: {word1}')
            print(f'Второе слово: {word2}')
            print(f'Функция И: {m.logic_and(word1, word2)}')
            print(f'Функция И-НЕ(Шеффера): {m.sheffer(word1, word2)}')
            print(f'Функция ДА(повторение 1-ого аргумента): {m.repeat_first(word1, word2)}')
            print(f'Функция НЕ(отрицание 1-ого аргумента): {m.negate_first(word1, word2)}')
        case 6:
            i1 = int(input('Введите индекс первого разрядного столбца: '))
            word1 = m.get_column(i1)
            i2 = int(input('Введите индекс второго разрядного столбца: '))
            word2 = m.get_column(i2)
            print(f'Первое слово: {word1}')
            print(f'Второе слово: {word2}')
            print(f'Функция И: {m.logic_and(word1, word2)}')
            print(f'Функция И-НЕ(Шеффера): {m.sheffer(word1, word2)}')
            print(f'Функция ДА(повторение 1-ого аргумента): {m.repeat_first(word1, word2)}')
            print(f'Функция НЕ(отрицание 1-ого аргумента): {m.negate_first(word1, word2)}')
        case 7:
            word = input('Введите слово(размером в длину матрицы): ')
            result = m.find_closest_word_below([int(word[i]) for i in range(len(word))])
            if result != None:
                print(result)
            else:
                print('Ближайшее значение снизу не найдено!')
        case 8:
            word = input('Введите слово(размером с длину матрицы): ')
            result = m.find_closest_word_above([int(word[i]) for i in range(len(word))])
            if result != None:
                print(result)
            else:
                print('Ближайшее значение сверху не найдено!')
        case 9:
            key = input('Введите ключ V(000-111): ')
            m.sum_A_and_B([int(key[i]) for i in range(len(key))])
            m.print_matrix()
        case 10:
            m.print_matrix()
        case 11:
            break
        case _:
            print('Введено число не от 1 до 9!')
