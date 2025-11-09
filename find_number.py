import os

# Ask the user which number to search
number_to_find = input("Enter the number to search (e.g., $100): ")

# Get all .txt files in the current folder
files = [f for f in os.listdir() if f.endswith(".txt")]

# Keep track if any matches are found
found_any = False

# Loop through all text files
for filename in files:
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            if number_to_find in line:
                print(f"Found in {filename}: {line.strip()}")
                found_any = True

# If nothing was found in any file
if not found_any:
    print(f"{number_to_find} not found in any file.")
