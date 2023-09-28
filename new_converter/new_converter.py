def perform_conversion(unit_1: str, unit_2: str, postman: float):
    str_value = input(f"Converting {unit_1} -> {unit_2}. Enter value (enter 'q' to exit): ")
    if str_value == "q":
        return True
    try:
        float_value = float(str_value)
    except ValueError:
        print("ERROR: You must enter a number.")
        return perform_conversion(unit_1, unit_2, postman)
    converted_value = round(float_value * postman, 2)
    print(f"Conversion result: {float_value} {unit_1} = {converted_value} {unit_2}.")
    return False

while True:
    print("Welcome to inches and centimeters converter!")
    print("1 - cm -> in.")
    print("2 - in -> cm.")
    choice = input("Your choice (1 or 2): ")
    if choice == "1" or choice == "2":
        break
    print("ERROR: Enter 1 or 2")

while True:
    if choice == "1":
        if perform_conversion("cm", "in", 0.394):
            break
    if choice == "2":
        if perform_conversion("in", "cm", 2.54):
            break
