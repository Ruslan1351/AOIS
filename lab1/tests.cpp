#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include "functions.h"

using namespace std;

TEST(transform_to_bin_codes, transform_to_bin_codes1) 
{ 
  int num = 10;
  Binary_Number direct_code, return_code, additional_code;
  to_binary_codes(num, direct_code, return_code, additional_code);

  print(num, direct_code, return_code, additional_code);


  vector <int> bin_num = {1,0,1,0};
  EXPECT_EQ(direct_code.sign, 0);
  EXPECT_EQ(direct_code.number, bin_num);
  
  EXPECT_EQ(return_code.sign, 0);
  EXPECT_EQ(return_code.number, bin_num);
  
  EXPECT_EQ(additional_code.sign, 0);
  EXPECT_EQ(additional_code.number, bin_num);
 
}

TEST(transform_to_bin_codes, transform_to_bin_codes2) 
{ 
    int num = -3;
    Binary_Number direct_code, return_code, additional_code;
    to_binary_codes(num, direct_code, return_code, additional_code);

    vector <int> dir_num = {1,1};
    EXPECT_EQ(direct_code.sign, 1);
    EXPECT_EQ(direct_code.number, dir_num);

    vector <int> ret_num = {0,0};
    EXPECT_EQ(return_code.sign, 1); 
    EXPECT_EQ(return_code.number, ret_num);
    
    vector <int> add_num = {0,1};
    EXPECT_EQ(additional_code.sign, 1);
    EXPECT_EQ(additional_code.number, add_num);
}

TEST(sum_add_codes, sum_add_codes1) { 
    int num1 = 6;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = 7;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number sum = binary_number_sum(additional_code1, additional_code2, num1 + num2);
    vector <int> add_sum = {1,1,0,1};
    EXPECT_EQ(sum.sign, 0);
    EXPECT_EQ(sum.number, add_sum);

    //print_result(sum, num1 + num2, "Сумма");

}

TEST(sum_add_codes, sum_add_codes2) 
{ 
    int num1 = 5;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = -7;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number sum = binary_number_sum(additional_code1, additional_code2, num1 + num2);
    vector <int> add_sum = {1,1,0};
    EXPECT_EQ(sum.sign, 1);
    EXPECT_EQ(sum.number, add_sum);
}

TEST(sum_add_codes, sum_add_codes3) 
{ 
    int num1 = -2;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = 9;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number sum = binary_number_sum(additional_code1, additional_code2, num1 + num2);
    vector <int> add_sum = {0,1,1,1};
    EXPECT_EQ(sum.sign, 0);
    EXPECT_EQ(sum.number, add_sum);
}

TEST(sum_add_codes, sum_add_codes4) 
{ 
    int num1 = -3;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = -5;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number sum = binary_number_sum(additional_code1, additional_code2, num1 + num2);
    vector <int> add_sum = {1,0,0,0};
    EXPECT_EQ(sum.sign, 1);
    EXPECT_EQ(sum.number, add_sum);
}

TEST(diff_add_codes, diff_add_codes1) { 
    int num1 = 10;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = 3;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number diff = binary_number_difference(additional_code1, additional_code2, num1, num2);
    vector <int> add_diff = {0,1,1,1};
    EXPECT_EQ(diff.sign, 0);
    EXPECT_EQ(diff.number, add_diff);

    //print_result(diff, num1 - num2, "Разность");
}

TEST(diff_add_codes, diff_add_codes2) 
{ 
    int num1 = -10;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = 5;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number diff = binary_number_difference(additional_code1, additional_code2, num1, num2);
    vector <int> add_diff = {0,0,0,1};
    EXPECT_EQ(diff.sign, 1);
    EXPECT_EQ(diff.number, add_diff);
}

TEST(diff_add_codes, diff_add_codes3) 
{ 
    int num1 = 4;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = -5;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number diff = binary_number_difference(additional_code1, additional_code2, num1, num2);
    vector <int> add_diff = {1,0,0,1};
    EXPECT_EQ(diff.sign, 0);
    EXPECT_EQ(diff.number, add_diff);
}

TEST(diff_add_codes, diff_add_codes4) { 
    int num1 = -3;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = -7;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number diff = binary_number_difference(additional_code1, additional_code2, num1, num2);
    vector <int> add_diff = {0,1,0,0};
    EXPECT_EQ(diff.sign, 0);
    EXPECT_EQ(diff.number, add_diff);
}

TEST(mult_dir_codes, mult_dir_codes1) 
{ 
    int num1 = 3;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = 5;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number mult = binary_number_multiplication(direct_code1, direct_code2);
    vector <int> dir_mult = {1,1,1,1};
    EXPECT_EQ(mult.sign, 0);
    EXPECT_EQ(mult.number, dir_mult);

   // print_result(mult, num1 * num2, "Произведение");
}

TEST(mult_dir_codes, mult_dir_codes2) 
{ 
    int num1 = -2;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = 10;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number mult = binary_number_multiplication(direct_code1, direct_code2);
    vector <int> dir_mult = {1,0,1,0,0};
    EXPECT_EQ(mult.sign, 1);
    EXPECT_EQ(mult.number, dir_mult);
}

TEST(mult_dir_codes, mult_dir_codes3) { 
    int num1 = -3;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = -7;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number mult = binary_number_multiplication(direct_code1, direct_code2);
    vector <int> dir_mult = {1,0,1,0,1};
    EXPECT_EQ(mult.sign, 0);
    EXPECT_EQ(mult.number, dir_mult);
}

TEST(div_dir_codes, div_dir_codes1) 
{ 
    int num1 = 3;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = 0;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number div = binary_number_dividing(direct_code1, direct_code2);
    vector <int> dir_div_num = {};
    vector <int> dir_div_fract = {};
    EXPECT_EQ(div.sign, 0);
    EXPECT_EQ(div.number, dir_div_num);
    EXPECT_EQ(div.fractional, dir_div_fract);
}

TEST(div_dir_codes, div_dir_codes2) 
{ 
    int num1 = 0;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = -7;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number div = binary_number_dividing(direct_code1, direct_code2);
    vector <int> dir_div_num = {0};
    vector <int> dir_div_fract = {0,0,0,0,0};
    EXPECT_EQ(div.sign, 1);
    EXPECT_EQ(div.number, dir_div_num);
    EXPECT_EQ(div.fractional, dir_div_fract);
}

TEST(div_dir_codes, div_dir_codes3) 
{ 
    int num1 = 10;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = 3;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number div = binary_number_dividing(direct_code1, direct_code2);
    vector <int> dir_div_num = {1,1};
    vector <int> dir_div_fract = {0,1,0,1,0};
    EXPECT_EQ(div.sign, 0);
    EXPECT_EQ(div.number, dir_div_num);
    EXPECT_EQ(div.fractional, dir_div_fract);

    print_binary_number(div);
}

TEST(div_dir_codes, div_dir_codes4) 
{ 
    int num1 = -4;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = 13;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number div = binary_number_dividing(direct_code1, direct_code2);
    vector <int> dir_div_num = {0};
    vector <int> dir_div_fract = {0,1,0,0,1};
    EXPECT_EQ(div.sign, 1);
    EXPECT_EQ(div.number, dir_div_num);
    EXPECT_EQ(div.fractional, dir_div_fract);
}

TEST(div_dir_codes, div_dir_codes5) 
{ 
    int num1 = -23;
    Binary_Number direct_code1, return_code1, additional_code1;
    to_binary_codes(num1, direct_code1, return_code1, additional_code1);
    int num2 = -2;
    Binary_Number direct_code2, return_code2, additional_code2;
    to_binary_codes(num2, direct_code2, return_code2, additional_code2);
   
    Binary_Number div = binary_number_dividing(direct_code1, direct_code2);
    vector <int> dir_div_num = {1,0,1,1};
    vector <int> dir_div_fract = {1,0,0,0,0};
    EXPECT_EQ(div.sign, 0);
    EXPECT_EQ(div.number, dir_div_num);
    EXPECT_EQ(div.fractional, dir_div_fract);
}

TEST(sum_float_nums, sum_float_nums1) 
{ 
    double num1 = 1.55;
    Floating_Point float_num1 = to_floating_point(num1);
    double num2 = 2.6;
    Floating_Point float_num2 = to_floating_point(num2);
    
    Floating_Point sum = floating_point_sum(float_num1, float_num2);
    vector <int> float_num_exp = {1,0,0,0,0,0,0,1};
    vector <int> float_num_mant = {0,0,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0};
    EXPECT_EQ(sum.sign, 0);
    EXPECT_EQ(sum.exponent, float_num_exp);
    EXPECT_EQ(sum.mantiss, float_num_mant);

    print_result(num1 + num2, sum, "Сумма");
}

TEST(sum_float_nums, sum_float_nums2) 
{ 
    double num1 = 0;
    Floating_Point float_num1 = to_floating_point(num1);
    double num2 = 2.6;
    Floating_Point float_num2 = to_floating_point(num2);
    
    Floating_Point sum = floating_point_sum(float_num1, float_num2);
    vector <int> float_num_exp = {1,0,0,0,0,0,0,0};
    vector <int> float_num_mant = {0,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0};
    EXPECT_EQ(sum.sign, 0);
    EXPECT_EQ(sum.exponent, float_num_exp);
    EXPECT_EQ(sum.mantiss, float_num_mant);
}

TEST(sum_float_nums, sum_float_nums3) 
{ 
    double num1 = 1.55;
    Floating_Point float_num1 = to_floating_point(num1);
    double num2 = 0;
    Floating_Point float_num2 = to_floating_point(num2);
    
    Floating_Point sum = floating_point_sum(float_num1, float_num2);
    vector <int> float_num_exp = {1,1,1,1,1,1,1};
    vector <int> float_num_mant = {1,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0};
    EXPECT_EQ(sum.sign, 0);
    EXPECT_EQ(sum.exponent, float_num_exp);
    EXPECT_EQ(sum.mantiss, float_num_mant);
}

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  ::testing::InitGoogleMock(&argc, argv);
  
  return RUN_ALL_TESTS();
}   