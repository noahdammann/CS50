from cs50 import get_float
import math

while True:
    change = get_float("How much change do I owe you? ")
    if change >= 0:
        break

# Calculate the number of quarters
change = change * 100
quarters = int((change / 25))
quarters = math.floor(quarters)
change = change % 25

# Calculate the number of dimes
dimes = int((change / 10))
dimes = math.floor(dimes)
change = change % 10

# Calculate the number of nickels
nickels = int((change / 5))
nickels = math.floor(nickels)
change = change % 5

# Calculate the number of pennies
pennies = int((change / 1))
pennies = math.floor(pennies)

# Sum the number of all the different coins
coins = quarters + dimes + nickels + pennies

# Print the sum of the coins
print(f"{coins}")