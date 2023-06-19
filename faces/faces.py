def main():
    user_input = input("Enter emoticon: ")
    converted_text = convert(user_input)
    print(converted_text)

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text



if __name__ == "__main__":
    main()