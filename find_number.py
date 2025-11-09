# Open the file in read mode
with open("sample.txt", "r") as file:
    lines = file.readlines()  # read all lines

# Loop through each line and check for $100
for line in lines:
    if "$100" in line:
        print("Found:", line.strip())
