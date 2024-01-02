from cs50 import get_int

# Get user input
while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

# Create loop
for i in range(height):
    for j in range(2 * height + 3):
        if i + j > height - 2 and j < height:
            print("#", end="")
        elif j < height:
            print(" ", end="")
        elif j == height + 1:
            print("  ", end="")
        elif j > height + 2 and i + j > height * 2 + 1:
            print("#", end="")
    print("")