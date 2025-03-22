#include "functions.h"
#include <iostream>
#include <cmath>

void print(vector <int> vector)
{
    for (auto i: vector)
        cout << i;
}

void print_binary_number(Binary_Number num)
{
    cout << num.sign << " ";
    print(num.number);
    if (num.fractional.size() != 0) {
        cout << ".";
        print(num.fractional);
    }
    cout << endl;
}

void print(int number_ten, Binary_Number direct_code, Binary_Number return_code, Binary_Number additional_code)
{
    cout << "Число в десятичной системе: " << number_ten << endl;
    cout << "Число в прямом коде: ";
    print_binary_number(direct_code);
    cout << "Число в обратном коде: ";
    print_binary_number(return_code);
    cout << "Число в дополнительном коде: ";
    print_binary_number(additional_code);
}

vector <int> to_binary_system(int number_ten)
{
    int quotient = abs(number_ten);
    vector <int> number_two = {};
    while (quotient >= 2)
    {
        number_two.insert (number_two.begin(), quotient % 2);
        quotient = quotient / 2;
    }
    number_two.insert (number_two.begin(), quotient);
    return number_two;
}

int find_max_number(int num1, int num2, int num3)  //3 3 4
{
    if (num1 >= num2)
        if (num1 >= num3)
            return num1;//
        else
            return num3;//
    else
        if (num2 >= num3)
            return num2;//
        else
            return num3; //
}

Binary_Number binary_number_sum(Binary_Number num1, Binary_Number num2, int sum) //6 7 13
{
    int bit_depth = find_max_number(num1.number.size(), num2.number.size(), to_binary_system(sum).size()); // 0110  + 0111  = 1101
    if (num1.sign == 0)                                                     
        while (num1.number.size() != bit_depth)  
            num1.number.insert(num1.number.begin(), 0);
    else
        while (num1.number.size() != bit_depth)
            num1.number.insert(num1.number.begin(), 1); 
    if (num2.sign == 0)                                                     
        while (num2.number.size() != bit_depth)  
            num2.number.insert(num2.number.begin(), 0);
    else
        while (num2.number.size() != bit_depth)
            num2.number.insert(num2.number.begin(), 1); 

    Binary_Number result;
    int memory = 0;
    int i = num1.number.size() - 1, j = num2.number.size() - 1;
    while (i != -1 and j != -1) 
    {
        result.number.insert(result.number.begin(), (num1.number[i] + num2.number[j] + memory) % 2);
        memory = (num1.number[i--] + num2.number[j--] + memory) / 2;
    }
    result.sign = (num1.sign + num2.sign + memory) % 2;
    return result;
}

void to_additional_or_direct_code(Binary_Number& num, int number_ten)
{
    for (int i = 0; i < num.number.size(); i++)
        if (num.number[i] == 1)
            num.number[i] = 0;
        else
            num.number[i] = 1;
    Binary_Number one;
    one.sign = 0;
    one.number = {1};
    num = binary_number_sum(num, one, number_ten + 1);
}

Binary_Number binary_number_difference(Binary_Number num1, Binary_Number num2, int number_ten1, int number_ten2) //num2-num1
{
    if (num2.sign == 0) {
        num2.sign = 1;
        to_additional_or_direct_code(num2, -number_ten2);
    }
    else {
        num2.sign = 0;
        to_additional_or_direct_code(num2, -number_ten2); 
    }
    return binary_number_sum(num1, num2, number_ten1 - number_ten2);
}

void to_binary_codes(int number_ten, Binary_Number& direct_code, Binary_Number& return_code, Binary_Number& additional_code)
{
    vector <int> number_two = to_binary_system(number_ten);
        direct_code.number = number_two;
        return_code.number = number_two;
        additional_code.number = number_two;
    if (number_ten >= 0)
    {
        direct_code.sign = 0;
        return_code.sign = 0;
        additional_code.sign = 0;
    }
    if (number_ten < 0)
    {
        direct_code.sign = 1;
        for (int i = 0; i < return_code.number.size(); i++)
            if (return_code.number[i] == 1)
                return_code.number[i] = 0;
            else
                return_code.number[i] = 1;
        return_code.sign = 1;
        Binary_Number one;
        one.sign = 0;
        one.number = {1};
        additional_code = binary_number_sum(return_code, one, number_ten + 1);
    }
}

Binary_Number binary_number_multiplication(Binary_Number num1, Binary_Number num2)
{
    Binary_Number multipl;
    if (num1.sign == num2.sign)
        multipl.sign = 0;
    else
        multipl.sign = 1;
    vector <vector<int>> terms;
    for (int i = num2.number.size() - 1; i != -1; i--) 
        if (num2.number[i] == 1)
            terms.push_back(num1.number);
        else
            terms.push_back(vector <int>(num1.number.size(), 0));
    for (int i = 1; i < terms.size(); i++)
        for (int j = 1; j <= i; j++)
            terms[i].push_back(0);
    vector <int> result = terms[0];
    for (int i = 1; i < terms.size(); i++) {
        if (result.size() < terms[i].size())
            result.insert(result.begin(), terms[i].size() - result.size(), 0);
        else
            terms[i].insert(terms[i].begin(), result.size() - terms[i].size(), 0);
        int memory = 0;
        int j = result.size() - 1;
        while (j >= 0) 
        {
            int sum = result[j] + terms[i][j] + memory;
            result[j--] = sum % 2;
            memory = sum / 2;
        }
        if (memory == 1)
            result.insert(result.begin(), 1);
    }
    multipl.number = result;
    return multipl;
}

bool binary_number1_bigger(vector <int> num1, vector <int> num2)  // >=
{
    while (num1.size() > 1 and num1[0] == 0)
        num1.erase(num1.begin());
    while (num1.size() > 1 and num2[0] == 0)
        num2.erase(num2.begin());
    if (num1.size() > num2.size())
        return 1;
    if (num1.size() < num2.size())
        return 0;
    if (num1.size() == num2.size()) {
        int i = 1, j = 1; 
        while (i != num1.size()) {
            if (num1[i] > num2[j])
                return 1;
            if (num1[i] < num2[j])
                return 0;
            i++; j++;
        }
    }
    return 1; //если равны
}

vector <int> binary_number_difference(vector <int> num1, vector <int> num2)
{
    while (num1.size() - num2.size() != 0)
        num2.insert(num2.begin(), 0);
    for (int i = 0; i < num2.size(); i++)
        if (num2[i] == 1)
            num2[i] = 0;
        else
            num2[i] = 1;
    int memory = 1;
    for (int i = num2.size() - 1; i >= 0; i--) {
        int sum = num2[i] + memory;
        num2[i] = sum % 2;
        memory = sum / 2;
    }
    memory = 0;
    vector <int> result;
    int i = num1.size() - 1;
    while (i >= 0) 
    {
        result.insert(result.begin(), (num1[i] + num2[i] + memory) % 2);
        memory = (num1[i] + num2[i--] + memory) / 2;
        
    }
    while (result.size() > 1 and result[0] == 0)
        result.erase(result.begin());
    return result;
}

Binary_Number binary_number_dividing(Binary_Number num1, Binary_Number num2) //num1/num2
{
    Binary_Number div;
    if (num1.sign == num2.sign)
        div.sign = 0;
    else
        div.sign = 1;
    vector <int> zero = { 0 }, one = {1};
    if (num2.number == zero) {
        cout << "Деление на 0!" << endl;
        return div;
    }
    if (num1.number == zero) {
        div.number = {0};
        div.fractional = {0,0,0,0,0};
        return div;
    }
    vector <int> current;
    div.number = {};
    for (int i = 0; i < num1.number.size(); i++) {
        current.push_back(num1.number[i]);
        if (binary_number1_bigger(current, num2.number)) {
            div.number.push_back(1);
            current  = binary_number_difference(current, num2.number);
        }
        else 
            div.number.push_back(0);      

    }
    while (div.number.size() > 1 and div.number[0] == 0)
        div.number.erase(div.number.begin());
    div.fractional = {};
    for (int i = 0; i < 5; i++) {
        current.push_back(0);
        if (binary_number1_bigger(current, num2.number)) {
            div.fractional.push_back(1);
            current  = binary_number_difference(current, num2.number);
        }
        else 
            div.fractional.push_back(0);      
    }
    return div;
}

void print_result(double number_ten, Floating_Point num, string str)
{
    cout << str << " в десятичной системе: " << number_ten << endl;
    cout << str << " в двоичной системе с плавающей точкой: " << num.sign << " ";
    print(num.exponent);
    cout << " ";
    print(num.mantiss); 
    cout << endl;
}

vector <int> to_binary_system(double num)
{
    vector <int> bin_num = to_binary_system((int)num);
    bin_num.push_back(-1); //переход к дробной части
    double fract_part = num - (int)num;
    while (bin_num.size() != 25) {
        fract_part *= 2;
        bin_num.push_back((int)fract_part);
        fract_part -= (int)fract_part;
    }
    return bin_num;
}

Floating_Point to_floating_point(double num)
{
    Floating_Point result;
    if (num == 0) {
        result.exponent = vector <int>(8, 0);
        result.mantiss = vector <int>(23, 0);
        return result;
    }
    vector <int> bin_num = to_binary_system(num);
    int int_part_size = 0;   
    while (bin_num[int_part_size] != -1)
        int_part_size++;
    bin_num.erase(bin_num.begin() + int_part_size);
    result.exponent = to_binary_system(int_part_size - 1 + 127);
    bin_num.erase(bin_num.begin());
    result.mantiss = bin_num;
    return result;
}

int to_decimal_system(vector <int> bin_num)
{
    int bit_depth = bin_num.size() - 1, result = 0;
    for (int i = 0; i < bin_num.size(); i++) 
        result += bin_num[i] * pow(2, bit_depth--);
    return result;

}

void align_exponents(Floating_Point& num1, Floating_Point& num2) {
    int exp1 = to_decimal_system(num1.exponent), exp2 = to_decimal_system(num2.exponent);
    if (exp1 > exp2) {
        int diff = exp1 - exp2;
        num2.exponent = num1.exponent;
        num2.mantiss.insert(num2.mantiss.begin(), 1);
        for (int i = 0; i < diff; i++) 
            num2.mantiss.insert(num2.mantiss.begin(), 0);
        num1.mantiss.insert(num1.mantiss.begin(), 1);
    } 
    if (exp2 > exp1) {
        int diff = exp2 - exp1;
        num1.exponent = num2.exponent;
        num1.mantiss.insert(num1.mantiss.begin(), 1);
        for (int i = 0; i < diff; i++) 
            num1.mantiss.insert(num1.mantiss.begin(), 0);
        num2.mantiss.insert(num2.mantiss.begin(), 1);
    }
}

Floating_Point floating_point_sum(Floating_Point num1, Floating_Point num2)
{
    Floating_Point result;
    align_exponents(num1, num2); 
    result.exponent = num1.exponent;
    while (num1.mantiss.size() > 24)
        num1.mantiss.pop_back();
    while (num2.mantiss.size() > 24)
        num2.mantiss.pop_back();
    vector<int> sum_mantiss;
    int memory = 0;
    for (int i = 23; i > 0; i--) {
        int sum = num1.mantiss[i] + num2.mantiss[i] + memory;
        sum_mantiss.insert(sum_mantiss.begin(), sum % 2);
        memory = sum / 2;
    }
    if ((num1.mantiss[0] + num2.mantiss[0] + memory) == 1) {
        result.mantiss = sum_mantiss;
        return result;
    }
    if ((num1.mantiss[0] + num2.mantiss[0] + memory) == 0) { 
        int exp = to_decimal_system(result.exponent);
        while (sum_mantiss[0] != 1) {
            sum_mantiss.erase(sum_mantiss.begin());
            sum_mantiss.push_back(0);
            exp--;
        }
        sum_mantiss.erase(sum_mantiss.begin());
        sum_mantiss.push_back(0);
        exp--;
        result.mantiss = sum_mantiss;
        result.exponent = to_binary_system(exp);
        return result;
    }
    if ((num1.mantiss[0] + num2.mantiss[0] + memory) > 1) { 
        int exp = to_decimal_system(result.exponent);
        sum_mantiss.insert(sum_mantiss.begin(), (num1.mantiss[0] + num2.mantiss[0] + memory) % 2);
        sum_mantiss.pop_back();
        exp++;
        result.mantiss = sum_mantiss;
        result.exponent = to_binary_system(exp);
        return result;
    }
}