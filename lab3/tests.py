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
        self.vars = ['a', 'b', 'c']

    def test_calc_minim_sknf(self):
        glued_sknf = f.glue_snf('sknf', self.sknf, self.vars)
        calc_minim_sknf = f.calc_minim_snf('sknf', glued_sknf)
        expect_calc_minim_sknf = '(b|c)&(!a|!c)'
        self.assertEqual(calc_minim_sknf, expect_calc_minim_sknf)

    def test_calc_minim_sdnf(self):
        glued_sdnf = f.glue_snf('sdnf', self.sdnf, self.vars)
        calc_minim_sdnf = f.calc_minim_snf('sdnf', glued_sdnf)
        expect_calc_minim_sdnf = '(!a&c)|(b&!c)'
        self.assertEqual(calc_minim_sdnf, expect_calc_minim_sdnf)

    def test_calc_table_minim_sknf(self):
        glued_sknf = f.glue_snf('sknf', self.sknf, self.vars)
        table, constituents, implicants = f.create_minim_table('sknf', self.sknf, glued_sknf)
        calc_table_minim_sknf = f.calc_table_minim_snf('sknf', table, implicants)
        expect_calc_table_minim_sknf = '(b|c)&(!a|!c)'
        self.assertEqual(calc_table_minim_sknf, expect_calc_table_minim_sknf)

    def test_calc_table_minim_sdnf(self):
        glued_sdnf = f.glue_snf('sdnf', self.sdnf, self.vars)
        table, constituents, implicants = f.create_minim_table('sdnf', self.sdnf, glued_sdnf)
        calc_table_minim_sdnf = f.calc_table_minim_snf('sdnf', table, implicants)
        expect_calc_table_minim_sdnf = '(!a&c)|(b&!c)'
        self.assertEqual(calc_table_minim_sdnf, expect_calc_table_minim_sdnf)

    def test_table_minim_sknf(self):
        map_karno, hor_values, vert_values = f.create_map_karno('sknf', self.sknf, 3)
        calc_minim_sknf = f.table_minim_snf('sknf', map_karno, hor_values, vert_values, self.vars)
        expect_calc_minim_sknf = '(b|c)&(!a|!c)'
        self.assertEqual(calc_minim_sknf, expect_calc_minim_sknf)

    def test_table_minim_sdnf(self):
        map_karno, hor_values, vert_values = f.create_map_karno('sdnf', self.sdnf, 3)
        calc_minim_sdnf = f.table_minim_snf('sdnf', map_karno, hor_values, vert_values, self.vars)
        expect_calc_minim_sdnf = '(b&!c)|(!a&c)'
        self.assertEqual(calc_minim_sdnf, expect_calc_minim_sdnf)

if __name__ == "__main__":
    unittest.main()