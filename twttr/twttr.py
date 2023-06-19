def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result

def main():
    word = input("Input: ")
    output = shorten(word)
    print("Output:", output)

if __name__ == "__main__":
    main()