import unittest
from functions import *

class TestLab6(unittest.TestCase):

    def setUp(self):
        self.table = HashTable()
        self.row = TableRow('ййй', '')

    def test_invalid_key1(self):
        valid = self.row.is_id_valid('kddkdk')
        self.assertEqual(valid, False)

    def test_invalid_key2(self):
        valid = self.row.is_id_valid('')
        self.assertEqual(valid, False)

    def test_invalid_key3(self):
        valid = self.row.is_id_valid('влвлв')
        self.assertEqual(valid, True)

    def test_add_and_get_row(self):
        row = TableRow('Иванов', 'Иван')
        self.table.add_row(row)
        find_row = self.table.get_row('Иванов')
        self.assertEqual(find_row, row)

        row = TableRow('Иванова', 'Инна')
        self.table.add_row(row)
        find_row = self.table.get_row('Иванова')
        self.assertEqual(find_row, row)

    def test_get_and_delete_row(self):
        row = TableRow('Иванов', 'Иван')
        self.table.add_row(row)
        find_row = self.table.get_row('Иванов')
        self.assertEqual(find_row, row)

        self.table.delete_row('Иванов')
        find_row = self.table.get_row('Иванов')
        self.assertEqual(find_row, None)

    def test_print_table(self):
        self.table.add_row(self.row)
        self.table.print_pretty_table()


if __name__ == "__main__":
    unittest.main()