from constants import *

class DiagonalMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def set_word(self, i, j, word: list):
        if len(word) == self.size:
            z = 0
            for k in range(i, self.size):
                self.matrix[k][j] = word[z]
                z += 1
            for k in range(i):
                self.matrix[k][j] = word[z]
                z += 1
        else:
            print('Размер слова не совпадает с размером матрицы!')

    def get_word(self, j):
        result = []
        for i in range(j, self.size):
            result.append(self.matrix[i][j])
        for i in range(j):
            result.append(self.matrix[i][j])
        return result

    def set_column(self, i, column: list):
        if (len(column) == self.size):
            for j in range(self.size):
                word_index = (j + i) % self.size
                self.matrix[word_index][j] = column[j]
        else:
            print('Размер столбца не совпадает с размером матрицы!')

    def get_column(self, i):
        column = []
        for j in range(self.size):
            word_index = (j + i) % self.size
            column.append(self.matrix[word_index][j])
        return column

    def logic_and(self, a, b):
        return [x & y for x, y in zip(a, b)]

    def sheffer(self, a, b):
        return [int(not (x & y)) for x, y in zip(a, b)]

    def repeat_first(self, a, b):
        return a[:]

    def negate_first(self, a, b):
        return [int(not x) for x in a]

    def find_closest_word_below(self, input_word):
        if len(input_word) != self.size:
            print('Длина слова не совпадает с размером матрицы!')
            return None
        closest_word = None
        for i in range(self.size):
            word = self.get_word(i)
            if word < input_word:
                if closest_word is None or word > closest_word:
                    closest_word = word
        return closest_word

    def find_closest_word_above(self, input_word):
        if len(input_word) != self.size:
            print('Длина слова не совпадает с размером матрицы!')
            return None
        closest_word = None
        for i in range(self.size):
            word = self.get_word(i)
            if word > input_word:
                if closest_word is None or word < closest_word:
                    closest_word = word
        return closest_word

    def find_columns_by_key(self, key):
        col_indexes = []
        for i in range(self.size):
            column = [self.matrix[j][i] for j in range(len(key))]
            if column == key:
                col_indexes.append(i)
        return col_indexes

    @staticmethod
    def sum_binary_numbers(num1, num2):
        n1, n2 = num1[:], num2[:]
        n1.insert(0, 0)
        n2.insert(0, 0)
        result, memory, i = [], 0, len(n1) - 1
        while i >= 0:
            result.insert(0, (n1[i] + n2[i] + memory) % 2)
            memory = (n1[i] + n2[i] + memory) // 2
            i -= 1
        return result

    def sum_A_and_B(self, key):
        if key not in KEYS:
            print('Ключ введен неверно!')
            return
        indexes = self.find_columns_by_key(key)
        for index in indexes:
            A = [self.matrix[j][index] for j in range(3, 7)]
            B = [self.matrix[j][index] for j in range(7, 11)]
            sum = self.sum_binary_numbers(A, B)
            new_column = key + A + B + sum
            self.set_word(0, index, new_column)

    def print_matrix(self):
        for j in range(self.size):
            row = '   '.join(str(bit) for bit in self.matrix[j])
            print(row)