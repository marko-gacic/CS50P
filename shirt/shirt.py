import sys
import os
from PIL import Image, ImageOps

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    sys.exit("Too few command-line arguments")

# Get the input and output file names
input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the file extensions are valid
valid_extensions = ['.jpg', '.jpeg', '.png']
input_ext = os.path.splitext(input_file)[1].lower()
output_ext = os.path.splitext(output_file)[1].lower()

if input_ext not in valid_extensions or output_ext not in valid_extensions:
    sys.exit("Invalid input or output file format")

# Check if the input file exists
if not os.path.exists(input_file):
    sys.exit("Input file does not exist")

if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

# Open the input file and resize it to the size of the shirt image
input_image = Image.open(input_file)
shirt = Image.open("shirt.png")
input_image = ImageOps.fit(input_image, shirt.size)

# Overlay the shirt image on the input image
input_image.paste(shirt, (0, 0), mask=shirt)

# Save the result to the output file
input_image.save(output_file)

print("Overlay completed")
