import random

NUMBER_MIN = 1
NUMBER_MAX = 10
NUMBER_OF_QUESTION = 4
right_answers = 0
wrong_answers = 0


def ask_a_question():
    a = random.randint(NUMBER_MIN, NUMBER_MAX)
    b = random.randint(NUMBER_MIN, NUMBER_MAX)

    response_str = input(f"Please, count: {a} + {b} = ")
    response_int = 0
    while response_int == 0:
        try:
            response_int = int(response_str)
        except:
            print(f"Please enter a number.")
            response_str = input(f"Please, count: {a} + {b} = ")
    if response_int == a + b:
        print(f"You gave the correct answer! {a} + {b} = {a + b}")
        return True

    print(f"Your Answer: {response_int}! Correct answer: {a} + {b} = {a + b}")
    return False


for i in range(0, NUMBER_OF_QUESTION):
    print(f"Question {i + 1} of {NUMBER_OF_QUESTION}.")
    if ask_a_question():
        right_answers += 1
    else:
        wrong_answers += 1
    print("----------------------------------")
print(f"Correct answers: {right_answers}! Wrong answers: {wrong_answers}.")
