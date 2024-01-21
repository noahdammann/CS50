from cs50 import get_int

# Ask user how many points they lost
points = get_int("How many points did you lose?" )

# If user achieved higher
if points < 2:
    print("You lost fewer points than me.")

# If user achived lower
elif points > 2:
    print("You lost more points than me.")

# If user achieved the same points
else:
    print("You lost the same number of points as me")