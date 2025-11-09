import os

number_to_find = input("Enter the number to search (e.g., $100): ")

# Get all .txt files in the 'data' folder
data_folder = "data"
files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith(".txt")]

found_any = False

for filename in files:
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            if number_to_find in line:
                print(f"Found in {filename}: {line.strip()}")
                found_any = True

if not found_any:
    print(f"{number_to_find} not found in any file.")
