import string

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for char in word:
        if char.isalpha() and char not in vowels:
            result += char
        elif char.isdigit():
            result += char
        elif char in string.punctuation:
            result += char
    return result

def main():
    word = input("Input: ")
    output = shorten(word)
    print("Output:", output)

if __name__ == "__main__":
    main()