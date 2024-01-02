from sys import argv, exit

if len(argv) != 2:
    print("Invalid command-line arguement")
    exit(1)

print(f"Hello, {argv[1]}")
exit(0)