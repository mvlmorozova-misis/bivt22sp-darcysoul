
import random
import math


def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)


def play_lcm(name):
    print("Find the smallest common multiple of given numbers.")
    for _ in range(3):
        numbers = [random.randint(1, 30) for _ in range(3)]
        correct_answer = lcm(lcm(numbers[0], numbers[1]), numbers[2])
        print(f"Question: {' '.join(map(str, numbers))}")
        answer = int(input("Your answer: "))

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
