import unittest
import lab3_functions as f


import sys
from pathlib import Path

lab2_path = str(Path(__file__).parent.parent / "lab2")
sys.path.append(lab2_path)

import functions as l2f
class TestLab3(unittest.TestCase):

    def setUp(self):
        self.sknf = '(a|b|c)&(!a|b|!c)&(!a|b|c)&(!a|!b|!c)'
        self.sdnf = '(!a&!b&c)|(!a&b&!c)|(!a&b&c)|(a&b&!c)'

    def test_calc_minim_sknf(self):
        calc_minim_sknf = f.calc_minim_snf('sknf', self.sknf, ['a', 'b', 'c'])
        expect_calc_minim_sknf = '(b|c)&(!a|!c)'
        self.assertEqual(calc_minim_sknf, expect_calc_minim_sknf)

    def test_calc_minim_sdnf(self):
        calc_minim_sdnf = f.calc_minim_snf('sdnf', self.sdnf, ['a', 'b', 'c'])
        expect_calc_minim_sdnf = '(!a&c)|(b&!c)'
        self.assertEqual(calc_minim_sdnf, expect_calc_minim_sdnf)

    def test_calc_table_minim_sknf(self):
        calc_minim_sknf = f.calc_table_minim_snf('sknf', self.sknf, ['a', 'b', 'c'])
        expect_calc_minim_sknf = '(b|c)&(!a|!c)'
        self.assertEqual(calc_minim_sknf, expect_calc_minim_sknf)

    def test_calc_table_minim_sdnf(self):
        calc_minim_sdnf = f.calc_table_minim_snf('sdnf', self.sdnf, ['a', 'b', 'c'])
        expect_calc_minim_sdnf = '(!a&c)|(b&!c)'
        self.assertEqual(calc_minim_sdnf, expect_calc_minim_sdnf)

    def test_table_minim_sknf(self):
        calc_minim_sknf = f.table_minim_snf('sknf', self.sknf, ['a', 'b', 'c'])
        expect_calc_minim_sknf = '(b|c)&(!a|!c)'
        self.assertEqual(calc_minim_sknf, expect_calc_minim_sknf)

    def test_table_minim_sdnf(self):
        calc_minim_sdnf = f.table_minim_snf('sdnf', self.sdnf, ['a', 'b', 'c'])
        expect_calc_minim_sdnf = '(b&!c)|(!a&c)'
        self.assertEqual(calc_minim_sdnf, expect_calc_minim_sdnf)

if __name__ == "__main__":
    unittest.main()