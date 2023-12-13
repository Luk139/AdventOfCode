# Read the contents of the file "AOC1.txt"
with open("AOC1.txt") as f:
    s = f.read()

# Initialize a variable to store the sum of first and last digits
sum_first_last_digits = 0

# Part 1: Calculate sum of first and last digits in each line
for line in s.strip().split("\n"):
    first_digit = None
    last_digit = None

    # Iterate through each character in the line
    for char in line:
        # Check if the character is a digit
        if char.isdigit():
            last_digit = char
            if first_digit is None:
                first_digit = char

    # If both first and last digits are found, add their sum to the total
    if first_digit is not None and last_digit is not None:
        sum_first_last_digits += int(first_digit + last_digit)

# Print the sum of the first and last digits in each line
print("Sum of first and last digits (Part 1):", sum_first_last_digits)


# Define a dictionary mapping words to their numeric representations
word_to_digit = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# Initialize a variable to store the sum of interpreted digits
sum_interpreted_digits = 0

# Part 2: Calculate sum of interpreted digits (from words and/or digits) in each line
for line in s.strip().split("\n"):
    first_digit = None
    last_digit = None
    interpreted_string = ""

    # Iterate through each character in the line
    for char in line:
        digit = None
        if char.isdigit():
            digit = char
        else:
            interpreted_string += char
            # Check if any word matches the end of the interpreted string
            for word, value in word_to_digit.items():
                if interpreted_string.endswith(word):
                    # Process the word as its corresponding digit value
                    digit = str(value)

        if digit is not None:
            last_digit = digit
            if first_digit is None:
                first_digit = digit

    # If both first and last digits are found, add their sum to the total
    if first_digit is not None and last_digit is not None:
        sum_interpreted_digits += int(first_digit + last_digit)

# Print the sum of interpreted digits (from words and/or digits) in each line
print("Sum of interpreted digits (Part 2):", sum_interpreted_digits)
