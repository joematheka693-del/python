# Create a function that:
# Takes no parameters
# Uses arithmetic operators to calculate the area of a rectangle
# Prints the result

length = 90
width = 40
Area = length * width
print("The area of the rectangle is: ", Area,"squared centimetre")

# Function With Parameters
# Create a function that:
# Accepts two numbers as parameters
# Returns their sum, difference, product, and division

def values(x, y):
    sum = x + y
    difference = x - y
    product = x * y
    division = x / y
    print("The answer is: ", sum)
    print("The answer is: ", difference)
    print("The answer is: ", product)
    print("The answer is: ", division)

values(40, 8)

# Control Statement (if...elif...else)
# Write a function that:
# Accepts a number (use input function)
# Checks whether the number is:
# Positive, Negative, Zero

number = int(input("Enter your number: "))

if number < 0 :
    print("Negative")
elif number == 0 :
    print("Zero")
else:
    print("Positive")

# Loop with Arithmetic
# Write a function that:
# Accepts a number n
# Uses a for loop
# Calculates the sum of numbers from 1 to n

number = int(input("Enter a number: "))

# While Loop
# Write a function that:
# Accepts a number (Use input() function)
# Uses a while loop
# Calculates the square of numbers from 1 up to that number

number = int(input("Enter a number: "))

while number < 50 :
    print(number ** 2)
    number = number + 1
