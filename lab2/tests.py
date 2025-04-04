import unittest
import functions as f

class TestLab2(unittest.TestCase):

    def setUp(self):
        self.log_func = '(a|b)&!c'
        self.true_table, self.variables = f.build_true_table(self.log_func)

    def test_build_true_table(self):
        true_table = [
            {'a': 0, 'b': 0, 'c': 0, self.log_func: 0},
            {'a': 0, 'b': 0, 'c': 1, self.log_func: 0},
            {'a': 0, 'b': 1, 'c': 0, self.log_func: 1},
            {'a': 0, 'b': 1, 'c': 1, self.log_func: 0},
            {'a': 1, 'b': 0, 'c': 0, self.log_func: 1},
            {'a': 1, 'b': 0, 'c': 1, self.log_func: 0},
            {'a': 1, 'b': 1, 'c': 0, self.log_func: 1},
            {'a': 1, 'b': 1, 'c': 1, self.log_func: 0},
        ]
        self.assertEqual(true_table, self.true_table)

    def test_build_sdnf(self):
        sdnf = '(!a&b&!c)|(a&!b&!c)|(a&b&!c)'
        self.assertEqual(sdnf, f.build_sdnf(self.true_table, self.log_func, self.variables))

    def test_build_sknf(self):
        sknf = '(a|b|c)&(a|b|!c)&(a|!b|!c)&(!a|b|!c)&(!a|!b|!c)'
        self.assertEqual(sknf, f.build_sknf(self.true_table, self.log_func, self.variables))

    def test_build_numeric_form_sdnf(self):
        numeric_form_sdnf = '(2, 4, 6) |'
        self.assertEqual(numeric_form_sdnf, f.build_numeric_form_sdnf(self.true_table, self.log_func, self.variables))

    def test_build_numeric_form_sknf(self):
        numeric_form_sknf = '(0, 1, 3, 5, 7) &'
        self.assertEqual(numeric_form_sknf, f.build_numeric_form_sknf(self.true_table, self.log_func, self.variables))

    def test_build_index_form(self):
        index_form = '42 - 00101010'
        self.assertEqual(index_form, f.build_index_form(self.true_table, self.log_func))

if __name__ == "__main__":
    unittest.main()