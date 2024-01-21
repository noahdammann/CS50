import sys

names = ["Ginny", "Ron", "Howard", "Penny", "Harry"]

if "Ron" in names:
    print("Found")
    sys.exit(0)

print("Not Found")
sys.exit(1)