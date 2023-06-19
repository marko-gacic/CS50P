import emoji

def emojize_text(text):
    emojized_text = emoji.emojize(text,  language='alias')
    return emojized_text

def main():
    text = input("Enter a text in English: ")
    emojized_text = emojize_text(text)
    print(emojized_text)

if __name__ == "__main__":
    main()