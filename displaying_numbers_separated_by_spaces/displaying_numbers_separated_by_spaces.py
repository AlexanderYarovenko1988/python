"""Пользователь вводит одно натуральное число из промежутка от 10 до 99 включительно. Программа выводит эти два числа раздельно
Пример:
Ввод - 23
Вывод - 2 3
"""


def user_input():
    while True:
        number_str = input("Enter a number from 10 to 99 (exit - q): ")
        if number_str == "q":
            return number_str
        try:
            if len(number_str) == 2:
                int(number_str)
                break
            else:
                print(f"You entered the value: {number_str}")
        except ValueError:
            print(f"You entered the value: {number_str}")
    return number_str


def user_output():
    while True:
        user_str = user_input()
        if user_str == "q":
            print("Goodbye!")
            break
        a = user_str[0]
        b = user_str[1]
        print(f"Enter - {user_str}")
        print(f"Output - {a} {b}")


user_output()
