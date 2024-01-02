from cs50 import get_int

n = get_int("n: ")

# Check for remainder
if n % 2 == 0:
    print("even")
else:
    print("odd")