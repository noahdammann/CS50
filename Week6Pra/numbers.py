import sys

numbers = [2, 4, 6, 8, 3, 5, 7, 0]
if 0 in numbers:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)