from constants import *

class TableRow:
    def __init__(self, id, data):
        if not self.is_id_valid(id.lower()):
            print('Ключ(ID) введен некорректно!')
            return
        self._id = id
        self._data = data
        if id != 'ььь':
            self.calc_decimal_value()
            self.calc_hash_value()
            self._U_flag = 1
        else:
            self._value = None
            self._hash = None
            self._U_flag = 0
        self._C_flag = 0
        self._D_flag = 0
        self._T_flag = 0
        self._L_flag = 1
        self._P0 = None

    def is_id_valid(self, id):
        for char in id:
            if char not in ALPHABET:
                return False
        if id == '':
            return False
        return True

    def calc_decimal_value(self):
        if len(self._id) == 1:
            self._value = ALPHABET.index(self._id[0].lower()) * 33
        else:
            self._value = ALPHABET.index(self._id[0].lower()) * 33 + ALPHABET.index(self._id[1].lower())

    def calc_hash_value(self):
        self._hash = self._value % H

class HashTable:
    def __init__(self):
        self._table = [TableRow('ььь', '')] * H
        self._keys = []

    def is_table_full(self):
       return all(self._table[i]._U_flag == 1 for i in range(H))

    def add_row(self, row: TableRow):
        if self.is_table_full():
            print('Таблица заполнена! Строка не добавлена!')
            return
        if self._table[row._hash]._U_flag == 0:
            self._table[row._hash] = row
            self._keys.append(row._id)
        else:
            self._table[row._hash]._C_flag = 1
            hash = row._hash
            while hash != H and self._table[hash]._U_flag == 1:
                hash += 1
            if hash != H:
                self._table[hash] = row
                self._keys.append(row._id)
            else:
                hash = row._hash
                while self._table[hash]._U_flag == 1:
                    hash -= 1
                self._table[hash] = row
                self._keys.append(row._id)

    def find_id(self, id):
        if id not in self._keys:
            print('Строки с таким ключом нет!')
            return -1
        if len(id) == 1:
            value = ALPHABET.index(id[0].lower()) * 33
        else:
            value = ALPHABET.index(id[0].lower()) * 33 + ALPHABET.index(id[1].lower())
        hash = value % H

        if self._table[hash]._id == id:
            return hash
        else:
            while hash != H and self._table[hash]._id != id:
                hash += 1
            if hash != H:
                return hash
            else:
                hash = value % H
                while self._table[hash]._id != id:
                    hash -= 1
                return hash

    def get_row(self, id):
        index = self.find_id(id)
        if index != -1:
            return self._table[index]
        else:
            return None

    def delete_row(self, id):
        index = self.find_id(id)
        if index != -1:
            self._table[index]._D_flag = 1
            self._table[index]._U_flag = 0
            self._keys.remove(id)

    def print_pretty_table(self):
        headers = [
            "Index", "ID", "Data", "Value", "Hash",
            "U_Flag", "C_Flag", "D_Flag", "T_Flag", "L_Flag", "P0"
        ]
        row_format = "{:<6} {:<10} {:<10} {:<6} {:<6} {:<7} {:<7} {:<7} {:<7} {:<7} {:<7}"
        print(row_format.format(*headers))
        print("-" * 80)

        for i in range(H):
            row = self._table[i]
            if row._D_flag == 1 or row._id == "ььь":
                id_display = ""
                data_display = ""
                value_display = ""
                hash_display = ""
                U_display = ""
                C_display = ""
                D_display = ""
                T_display = ""
                L_display = ""
                P0_display = ""
            else:
                id_display = row._id
                data_display = row._data
                value_display = row._value
                hash_display = row._hash
                U_display = row._U_flag
                C_display = row._C_flag
                D_display = row._D_flag
                T_display = row._T_flag
                L_display = row._L_flag
                P0_display = row._P0
            print(row_format.format(
                i,
                id_display,
                data_display,
                value_display,
                hash_display,
                U_display,
                C_display,
                D_display,
                T_display,
                L_display,
                row._P0 if row._P0 is not None else ""
            ))