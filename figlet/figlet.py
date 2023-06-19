from pyfiglet import Figlet
import sys
import random

def main():
    if len(sys.argv) == 1:
        font_name = get_random_font()
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font' ):
        font_name = sys.argv[2]
    else:
        print_usage_and_exit()

    figlet = Figlet(font=font_name)
    user_input = input("Enter text: ")
    print(figlet.renderText(user_input))


def print_usage_and_exit():
    print("Usage: figlet.py [-f <font_name>] ")
    sys.exit(1)

def get_random_font():
    figlet = Figlet()
    fonts = figlet.getFonts()
    return random.choice(fonts)


main()
