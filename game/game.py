import random


def main():
    level = get_level()
    secret_number = random.randint(1, level)

    while True:
        guess = get_guess()

        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
            else:
                print("Enter a positive int")
        except ValueError:
            print("Enter a valid int")

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
            else:
                print("Enter a positive int")
        except ValueError:
            print("Enter a valid int")

main()