import cs50
from cs50 import get_string

sentence = get_string("Sentence: ")

# Count the number of words
words = 1
empty_space = ' '
for c in sentence:
    if c == empty_space:
        words += 1

# Count the number of letters
letters = 0
for i in range(len(sentence)):
    if sentence[i].isalpha():
        letters += 1

# Count the number of sentences
sentences = 0
for i in range(len(sentence)):
    if sentence[i] == '.' or sentence[i] == '?' or sentence[i] == '!':
        sentences += 1

# Calculate the reading level
L = letters / words * 100
S = sentences / words * 100
grade = 0.0588 * L - 0.296 * S - 15.8
grade = round(grade)

# Print the grade
if grade > 0 and grade < 15:
    print(f"Grade {grade}")
elif grade < 1:
    print("Before Grade 1")
else:
    print("Grade 16+")