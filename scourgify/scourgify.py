import sys
import csv
import os

if len(sys.argv) != 3:
    sys.exit("Too few command-line arguments")

input_filename = sys.argv[1]
output_filename = sys.argv[2]

if not os.path.exists(input_filename):
    sys.exit("Input file does not exist")

try:
    with open(input_filename) as input_file, open(output_filename, 'w', newline='') as output_file:
        reader = csv.DictReader(input_file)
        writer = csv.DictWriter(output_file, fieldnames=['first', 'last', 'house'])
        writer.writeheader()

        for row in reader:
            name = row['name']
            last_name, first_name = map(str.strip, name.split(',', 1))

            writer.writerow({'first': first_name, 'last': last_name, 'house': row['house']})

    print("Conversion complete!")
except FileNotFoundError:
    sys.exit("Input file not found")
