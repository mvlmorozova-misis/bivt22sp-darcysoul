
import random


def generate_progression(start, factor, length):
    return [start * (factor ** i) for i in range(length)]


def play_progression(name):
    print("What number is missing in the progression?")

    for _ in range(3):
        length = random.randint(5, 10)
        start = random.randint(1, 10)
        factor = random.randint(2, 5)
        progression = generate_progression(start, factor, length)
        hidden_index = random.randint(0, length - 1)
        correct_answer = progression[hidden_index]
        progression[hidden_index] = '..'
        print(f"Question: {' '.join(map(str, progression))}")

        answer = int(input("Your answer: "))

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
