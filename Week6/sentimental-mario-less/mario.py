from cs50 import get_int

# Prompt user for input
while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

# Loop function
for i in range(height):
    for j in range(height):
        if i + j > height - 2:
            print("#", end="")
        else:
            print(" ", end="")
    print("")