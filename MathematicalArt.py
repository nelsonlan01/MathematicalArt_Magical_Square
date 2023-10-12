import random

# Get user input for size of the 2D array
n = int(input("Enter the size of the array: "))

# Create a String variable called s and store 0-9 inside
s = "0123456789"

# Define a function to generate a single array
def generate_array():
    # Create a 2D array of size n x n and initialize it to 0
    arr = [[0 for j in range(n)] for i in range(n)]

    # Fill the first row of the array with randomly chosen items from a substring of s, ensuring no repeats
    row_items = set()  # keep track of items already chosen in this row
    for i in range(n):
        while True:
            item = random.choice(s[:n])
            if item not in row_items:
                arr[0][i] = item
                row_items.add(item)
                break

    # Fill the remaining rows of the array with randomly chosen items from a substring of s, ensuring no repeats within the row and no repeats with the corresponding indices of the previous row
    for i in range(1, n):
        current_row = arr[i]
        row_items = set()  # keep track of items already chosen in this row
        for j in range(n):
            while True:
                item = random.choice(s[:n])
                if item not in row_items and item not in [arr[k][j] for k in range(i)]:
                    current_row[j] = item
                    row_items.add(item)
                    break

    # Return the array
    return arr

# Get user input for the number of sets to generate
y = int(input("Enter the number of sets to generate: "))

# Generate y sets of the same array
arrays = [generate_array() for _ in range(y)]

# Join the arrays together element by element with commas
result = []
for i in range(n):
    row = ""
    for j in range(n):
        row += str(arrays[0][i][j])
        for k in range(1, y):
            row += "," + str(arrays[k][i][j])
        row += " "
    result.append(row)

# Print the resulting arrays row by row
for row in result:
    print(row)
