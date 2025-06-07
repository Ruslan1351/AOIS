import unittest
from functions import *

class TestLab7(unittest.TestCase):

    def setUp(self):
        self.m = DiagonalMatrix(16)

    def test_add_and_get_word(self):
        word = [1] * 16
        self.m.set_word(0, 0, word)
        self.assertEqual(self.m.get_word(0), word)

    def test_add_and_get_column(self):
        column = [1] * 16
        self.m.set_column(0, column)
        result = self.m.get_column(0)
        self.assertEqual(result, column)

    def test_logic_and(self):
        a = [1, 0, 1, 1]
        b = [1, 1, 0, 1]
        expected = [1, 0, 0, 1]
        self.assertEqual(self.m.logic_and(a, b), expected)

    def test_sheffer(self):
        a = [1, 0, 1, 1]
        b = [1, 1, 0, 1]
        expected = [0, 1, 1, 0]
        self.assertEqual(self.m.sheffer(a, b), expected)

    def test_repeat_first(self):
        a = [0, 1, 0, 1]
        b = [1, 1, 1, 1]
        self.assertEqual(self.m.repeat_first(a, b), a)

    def test_repeat_last(self):
        a = [0, 1, 0, 1]
        b = [1, 1, 1, 1]
        self.assertEqual(self.m.negate_first(b, a), [0, 0, 0, 0])

    def test_find_closest_value(self):
        self.m.set_word(0, 0, [0] * 15 + [1])
        self.m.set_word(0, 1, [1] * 16)
        input_word = [0] * 15 + [0]
        result = self.m.find_closest_word_above(input_word)
        self.assertEqual(result, [0] * 15 + [1])
        result = self.m.find_closest_word_below([1] * 16)
        self.assertEqual(result, [0] * 15 + [1])

    def test_sum_A_and_B(self):
        from constants import KEYS
        key = KEYS[0] if KEYS else [0, 1, 0]
        word = key + [1, 0, 1, 1] + [0, 1, 0, 1]
        self.m.set_word(0, 0, word + [0] * 5)
        self.m.sum_A_and_B(key)
        expected_sum = [1, 0, 0, 0, 0]
        result = self.m.get_word(0)[11:16]
        self.assertEqual(result, expected_sum)

    def test_print_matrix(self):
        self.m.print_matrix()


if __name__ == "__main__":
    unittest.main()