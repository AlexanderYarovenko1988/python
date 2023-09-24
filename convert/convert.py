def unit_of_length():
    while True:
        user_input = input("CM - to convert centimeters to inches. IN - to convert inches to centimeters: ")
        try:
            if user_input in ("CM", "IN"):
                return user_input
        except ValueError:
            print("ERROR!")


def getting_number_user():
    while True:
        centimeters_str = input("Enter a number: ")
        try:
            centimeters_float = float(centimeters_str)
            return centimeters_float
        except ValueError:
            print("ERROR!")


def convert_inches():
    user_input = unit_of_length()
    user_float = getting_number_user()
    inch_to_cm = 2.54
    if user_input == "CM":
        print(f"{user_float} centimeter is {user_float / inch_to_cm} inch")
    elif user_input == "IN":
        print(f"{user_float} inch is {user_float * inch_to_cm} centimeter")


convert_inches()
