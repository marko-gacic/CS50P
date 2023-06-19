import random

def main():
    words = ['python', 'hangman', 'game', 'programming', 'harvard', 'computer']
    word = random.choice(words)
    play_hangman(word)

def play_hangman(word):
    guessed_letters = []
    tries = 6

    while tries > 0:
        guessed_word = ""

        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        print("Guess the word:", guessed_word)
        print("Tries left:", tries)

        if guessed_word == word:
            print("Congratulations! You guessed the word correctly.")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print("Wrong guess.")

        print()

    if tries == 0:
        print("Oops! You ran out of tries. The word was:", word)

if __name__ == "__main__":
    main()
