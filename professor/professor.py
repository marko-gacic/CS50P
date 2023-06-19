import random

def main():
    level = get_level()
    problems = generate_problems(level)
    score = solve_problems(problems)
    print("Your score: {}/10".format(score))


def get_level():
    while True:
        level = input("Level: ")
        if level in ['1', '2', '3']:
            return int(level)
        else:
            print("Invalid level. Please try again.")

def generate_problems(level):
    problems = []
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = "{} + {} = ".format(x, y)
        problems.append((x, y, problem))
    return problems


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")



def solve_problems(problems):
    score = 0
    for x, y, problem in problems:
        print(problem)
        for _ in range(3):
            answer = input("Answer: ")
            try:
                if int(answer) == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print("Correct answer is: {}".format(x + y))
    return score


if __name__ == "__main__":
    main()