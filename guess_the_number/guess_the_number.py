import random

def get_user_number(min_num, max_num):
    int_number = 0
    while int_number == 0:
        str_number = input(f"Введите число от {min_num} до {max_num}: ")
        try:
            int_number = int(str_number)
        except ValueError:
            print(f"Вы ввели не число. Введите значение от {min_num} до {max_num}.")
        else:
            if int_number < min_num:
                print(f"Введите число больше или равное {min_num}")
                int_number = 0
            elif int_number > max_num:
                print(f"Введите число меньше или равное {max_num}")
                int_number = 0
    return int_number

def main():
    min_number = 1
    max_number = 10
    random_number = random.randint(min_number, max_number)
    number_of_lives = 5
    life = number_of_lives

    while life > 0:
        print(f"Количество оставшихся жизней: {life}.")
        user_number = get_user_number(min_number, max_number)
        if user_number == random_number:
            print(f"Вы угадали число! Это {random_number}")
            print(f"Количество оставшихся жизней: {life}.")
            break
        elif user_number > random_number:
            print(f"Ваше число больше загаданного! Попробуйте еще раз.")
            life -= 1
        elif life == 1:
            print(f"Вы проиграли. Загаданное число {random_number}")
            life -= 1
            print(f"Количество оставшихся жизней: {life}.")
        else:
            print(f"Ваше число меньше загаданного! Попробуйте еще раз.")
            life -= 1

if __name__ == "__main__":
    main()
