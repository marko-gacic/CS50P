def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s[2:].isalnum() or s[2].isdigit() or '0' in s[2:]:
        return False
    return True

if __name__ == "__main__":
    main()
