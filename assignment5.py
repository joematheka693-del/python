# Create a function that:
# Takes no parameters
# Uses arithmetic operators to calculate the area of a rectangle
# Prints the result

def area():
    length = 90
    width = 40
    area = length * width
    print(area)
area()

print("===============================================================")
# Function With Parameters
# Create a function that:
# Accepts two numbers as parameters
# Returns their sum, difference, product, and division

def values(x, y):
    sum = x + y
    difference = x - y
    product = x * y
    division = x / y
    print("The sum is: ", sum)
    print("The diffference is: ", difference)
    print("The product is: ", product)
    print("The quotient is: ", division)

values(40, 8)

print("===============================================================")
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

print("===============================================================")
# Loop with Arithmetic
# Write a function that:
# Accepts a number n
# Uses a for loop
# Calculates the sum of numbers from 1 to n

def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_to_n(100))


print("===============================================================")
# While Loop
# Write a function that:
# Accepts a number (Use input() function)
# Uses a while loop
# Calculates the square of numbers from 1 up to that number

number = int(input("Enter a number: "))

while number < 50 :
    print(number ** 2)
    number = number + 1
