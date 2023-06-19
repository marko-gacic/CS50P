import sys
import os

def is_comment(line):
    line = line.strip()
    return line.startswith('#')

def is_docstring(line, in_docstring):
    line = line.strip()
    if in_docstring:
        return not (line.endswith('"""') or line.endswith("'''"))
    return line.startswith('"""') or line.startswith("'''") or line.startswith('r"""') or line.startswith("r'''")

def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    count = 0
    in_docstring = False

    for line in lines:
        if is_docstring(line, in_docstring):
            in_docstring = not in_docstring
        elif not is_comment(line) and not in_docstring and line.strip():
            count += 1

    return count

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith('.py'):
        sys.exit("Not a Python file")

    if not os.path.exists(filename):
        sys.exit("File does not exist")

    try:
        line_count = count_lines(filename)
        print(f"{line_count}")
    except FileNotFoundError:
        sys.exit("File not found")
