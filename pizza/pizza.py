import sys
import csv
from tabulate import tabulate
import os

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments")

filename = sys.argv[1]

if not filename.endswith('.csv'):
    sys.exit("Not a CSV file")

if not os.path.exists(filename):
    sys.exit("File does not exist")

try:
    with open(filename) as file:
        reader = csv.DictReader(file)
        table = [list(row.values()) for row in reader]

    headers = list(reader.fieldnames)
    ascii_table = tabulate(table, headers=headers, tablefmt="grid")
    print(ascii_table)
except FileNotFoundError:
    sys.exit("File not found")
