#include <string>
#include <vector>

using namespace std;

struct Binary_Number
{
    int sign;
    vector <int> number;
    vector <int> fractional;
};

struct Floating_Point
{
    int sign = 0;
    vector <int> exponent;
    vector <int> mantiss;
};

void print(vector <int> vector);

void print_binary_number(Binary_Number num);

void print(int number_ten, Binary_Number direct_code, Binary_Number return_code, Binary_Number additional_code);

vector <int> to_binary_system(int number_ten);

int find_max_number(int num1, int num2, int num3);  

Binary_Number binary_number_sum(Binary_Number num1, Binary_Number num2, int sum); 

void to_additional_or_direct_code(Binary_Number& num, int number_ten);

Binary_Number binary_number_difference(Binary_Number num1, Binary_Number num2, int number_ten1, int number_ten2);//num2-num1

void to_binary_codes(int number_ten, Binary_Number& direct_code, Binary_Number& return_code, Binary_Number& additional_code);

Binary_Number binary_number_multiplication(Binary_Number num1, Binary_Number num2);

bool binary_number1_bigger(vector <int> num1, vector <int> num2);  // >=

vector <int> binary_number_difference(vector <int> num1, vector <int> num2);

Binary_Number binary_number_dividing(Binary_Number num1, Binary_Number num2); //num1/num2
    
void print_result(double number_ten, Floating_Point num, string str);

vector <int> to_binary_system(double num);

Floating_Point to_floating_point(double num);

int to_decimal_system(vector <int> bin_num);

void align_exponents(Floating_Point& num1, Floating_Point& num2);

Floating_Point floating_point_sum(Floating_Point num1, Floating_Point num2);