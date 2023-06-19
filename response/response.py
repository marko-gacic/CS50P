import validators

def main():
    email = input("What is your email address? ")
    validate(email)


def validate(email):
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()