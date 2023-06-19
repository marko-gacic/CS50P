import sys
import inflect

def main():
    names = []
    print("Name: ")

    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        if len(names) > 0:
            bid_adieu(names)
        else:
            print("Please enter name")


def bid_adieu(names):
    p = inflect.engine()
    count = len(names)

    for i, name in enumerate(names):
        if count == 1:
            print(f"Adieu, adieu, to {name}")
        elif count == 2:
            if i == 0:
                print(f"Adieu, adieu, to {name} and", end=" ")
            else:
                print(name)
        else:
            if i == 0:
                print(f"Adieu, adieu, to {name},", end=" ")
            elif i == count - 1:
                print(f"and {name}")
            else:
                print(name, end=", ")

main()