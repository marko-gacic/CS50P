def main():
    user_answer = question()
    result = answer(user_answer)
    print(result)

def question():
    question = input("What is the answer to the question of life, the Universe, and Everything? ")
    return question

def answer(answer):
    answer = answer.lower().replace("-", "").replace(" ", "")
    if answer == "42" or answer == "fortytwo":
        return "Yes"
    else:
        return "No"






main()