# pattern_drawing.py

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for each row
while row < size:
    # For loop for each column in the row
    for col in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1