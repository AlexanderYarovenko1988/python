def unit_of_length():
    while True:
        user_input = input("СМ - для перобразования сантиметров в дюймы. ДМ - для преобразования дюймов в сантиметры: ")
        try:
            if user_input in ("СМ", "ДМ"):
                return user_input
        except ValueError:
            print("ERROR!")

def getting_number_user():
    while True:
        centimeters_str = input("Введите число: ")
        try:
            centimeters_float = float(centimeters_str)
            return centimeters_float
        except ValueError:
            print("ERROR!")


def convert_inches():
    user_input = unit_of_length()
    user_float = getting_number_user()
    dm = 2.54
    if user_input == "СМ":
        print(user_float * dm)
    elif user_input == "ДМ":
        print(user_float / dm)


convert_inches()
