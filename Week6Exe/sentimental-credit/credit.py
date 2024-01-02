from cs50 import get_int
import math

# Prompt user for input
num = get_int("Card Number: ")
card = num
card2 = num
card_start = num

# Find the number of digits in the card
length = 0
while num > 1:
    num = num / 10
    length += 1

# Find every second digit
leng = int(length / 2)
nums = [x for x in range(leng)]
for i in range(leng):
    card = math.floor(card / 10)
    value = card % 10
    card = card / 10
    nums[i] = value

# Multiply every second digit by 2
numbers = [x for x in range(leng)]
for i in range(leng):
    temp = nums[i]
    numbers[i] = temp * 2

# Create single digits out of numbers
digits = []
for i in range(leng):
    if numbers[i] > 9:
        digits.append(math.floor(numbers[i] / 10))
        digits.append(numbers[i] % 10)
    else:
        digits.append(numbers[i])

# Add single digits together
total1 = sum(digits)

# Get the remaining digits in card
remaining_digits = []
for i in range(leng + 1):
    digit2 = (card2 % 10)
    card2 = math.floor(card2 / 100)
    remaining_digits.append(digit2)

# Add the remaining digits together
total2 = sum(remaining_digits)

# Add the totals together
total = total1 + total2

# Collect the first two digits
len1 = length - 2
first2digits = math.floor(card_start / 10 ** len1)

# Collect the first digit
len2 = length - 1
first1digits = math.floor(card_start / 10 ** len2)

# Print the card type
if total % 10 != 0:
    print("INVALID")
elif length == 15 and first2digits == 34 or first2digits == 37:
    print("AMEX")
elif length == 16 and first2digits > 50 and first2digits < 56:
    print("MASTERCARD")
elif length == 13 or length == 16 and first1digits == 4:
    print("VISA")
else:
    print("INVALID"
    )