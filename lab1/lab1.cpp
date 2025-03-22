#include <iostream>
#include <cmath>
#include "functions.h"

template <typename T> void print_result(Binary_Number binary_result, T decimal_result, string operation)
{
    Binary_Number direct_code, return_code, additional_code;
    to_binary_codes(decimal_result, direct_code, return_code, additional_code);
    cout << operation << " в десятичной системе: " << decimal_result << endl;
    if (operation == "Сумма" or operation == "Разность") {
        cout << operation << " в прямом коде: ";
        print_binary_number(direct_code);
        cout << operation << " в обратном коде: ";
        print_binary_number(return_code);
        cout << operation << " в дополнительном коде: ";
        print_binary_number(binary_result);
    }
    if (operation == "Произведение") {
        cout << operation << " в прямом коде: ";
        print_binary_number(binary_result);
        cout << operation << " в обратном коде: ";
        print_binary_number(return_code);
        cout << operation << " в дополнительном коде: ";
        print_binary_number(additional_code);
    }
    if (operation == "Частное") {
        cout << operation << " в прямом коде: ";
        print_binary_number(binary_result);
        if (binary_result.sign == 0) {
            cout << operation << " в обратном коде: ";
            print_binary_number(binary_result);
            cout << operation << " в дополнительном коде: ";
            print_binary_number(binary_result);
        }
        else {
            return_code.fractional = binary_result.fractional;
            for (int i = 0; i < return_code.fractional.size(); i++)
                if (return_code.fractional[i] == 1)
                    return_code.fractional[i] = 0;
                else
                    return_code.fractional[i] = 1;
            additional_code.fractional = return_code.fractional;
            cout << operation << " в обратном коде: ";
            print_binary_number(return_code);
            cout << operation << " в дополнительном коде: ";
            print_binary_number(additional_code);
        }
    }
}

int main()
{
    setlocale(0, "");
    int flag = 1;
    while (flag == 1) {
        int key;
        cout << "Выберите действие(введите число):" << endl;
        cout << "1 - перевод" << endl;
        cout << "2 - сложение в дополнительном коде" << endl;
        cout << "3 - вычитание в дополнительном коде" << endl;
        cout << "4 - умножение в прямом коде" << endl;
        cout << "5 - деление в прямом коде" << endl;
        cout << "6 - сложение положительных чисел с плавающей точкой" << endl;
        cout << "7 - выход из меню" << endl;
        cin >> key;
        switch (key) 
        {
        case 1:
        {
            cout << "Введите число в десятичной системе: ";
            int number_ten;
            cin >> number_ten;
            Binary_Number direct_code, return_code, additional_code;
            to_binary_codes(number_ten, direct_code, return_code, additional_code);
            print(number_ten, direct_code, return_code, additional_code);
            break;
        }
        case 2:
        {
            cout << "Введите первое число в десятичной системе: ";
            int number_ten1;
            cin >> number_ten1;
            cout << "Введите второе число в десятичной системе: ";
            int number_ten2;
            cin >> number_ten2;
            cout << endl;
            Binary_Number direct_code1, return_code1, additional_code1;
            to_binary_codes(number_ten1, direct_code1, return_code1, additional_code1);
            print(number_ten1, direct_code1, return_code1, additional_code1);
            cout << endl;
            Binary_Number direct_code2, return_code2, additional_code2;
            to_binary_codes(number_ten2, direct_code2, return_code2, additional_code2);
            print(number_ten2, direct_code2, return_code2, additional_code2);
            cout << endl;
            print_result(binary_number_sum(additional_code1, additional_code2, number_ten1 + number_ten2), number_ten1 + number_ten2, "Сумма");
            break;
        }
        case 3:
        {
            cout << "Введите первое число(уменьшаемое) в десятичной системе: ";
            int number_ten1;
            cin >> number_ten1;
            cout << "Введите второе число(вычитаемое) в десятичной системе: ";
            int number_ten2;
            cin >> number_ten2;
            cout << endl;
            Binary_Number direct_code1, return_code1, additional_code1;
            to_binary_codes(number_ten1, direct_code1, return_code1, additional_code1);
            print(number_ten1, direct_code1, return_code1, additional_code1);
            cout << endl;
            Binary_Number direct_code2, return_code2, additional_code2;
            to_binary_codes(number_ten2, direct_code2, return_code2, additional_code2);
            print(number_ten2, direct_code2, return_code2,  additional_code2);
            cout << endl;
            print_result(binary_number_difference(additional_code1, additional_code2, number_ten1, number_ten2), number_ten1 - number_ten2, "Разность");
            break;
        }
        case 4:
        {
            cout << "Введите первое число в десятичной системе: ";
            int number_ten1;
            cin >> number_ten1;
            cout << "Введите второе число в десятичной системе: ";
            int number_ten2;
            cin >> number_ten2;
            cout << endl;
            Binary_Number direct_code1, return_code1, additional_code1;
            to_binary_codes(number_ten1, direct_code1, return_code1, additional_code1);
            print(number_ten1, direct_code1, return_code1, additional_code1);
            cout << endl;
            Binary_Number direct_code2, return_code2, additional_code2;
            to_binary_codes(number_ten2, direct_code2, return_code2, additional_code2);
            print(number_ten2, direct_code2, return_code2, additional_code2);
            cout << endl;
            print_result(binary_number_multiplication(direct_code1, direct_code2), number_ten1 * number_ten2, "Произведение");
            break;
        }
        case 5:
        {
            cout << "Введите первое число в десятичной системе: ";
            int number_ten1;
            cin >> number_ten1;
            cout << "Введите второе число в десятичной системе: ";
            int number_ten2;
            cin >> number_ten2;
            cout << endl;
            Binary_Number direct_code1, return_code1, additional_code1;
            to_binary_codes(number_ten1, direct_code1, return_code1, additional_code1);
            print(number_ten1, direct_code1, return_code1, additional_code1);
            cout << endl;
            Binary_Number direct_code2, return_code2, additional_code2;
            to_binary_codes(number_ten2, direct_code2, return_code2, additional_code2);
            print(number_ten2, direct_code2, return_code2, additional_code2);
            cout << endl;
            
            
            vector <int> nothing = {};
            if (binary_number_dividing(direct_code1, direct_code2).number != nothing)
                print_result(binary_number_dividing(direct_code1, direct_code2), round(100000 * double(number_ten1) / double(number_ten2)) / 100000, "Частное");
            break;
        }
        case 6:
        {
            cout << "Введите первое число в десятичной системе: ";
            double number_ten1;
            cin >> number_ten1;
            cout << "Введите второе число в десятичной системе: ";
            double number_ten2;
            cin >> number_ten2;
            cout << endl;
            Floating_Point number1 = to_floating_point(number_ten1), number2 = to_floating_point(number_ten2);
            print_result(number_ten1, number1, "Число");
            print_result(number_ten2, number2, "Число");
            print_result(number_ten1 + number_ten2, floating_point_sum(number1, number2), "Сумма");
            break;
        }
        case 7:
        {

            flag = 2;
            break;
        }
        default:
            cout << "Введено число не от 1 до 30!" << endl;
        }
    }  
}
