# Python while loop.
# While loop executes a block of code repeatedly as long as a certain condition is true. The syntax of a while loop in python is as follows.
"""
Initializing of a variable,
while keyword,
followed by the condition/statement to be evaluated,
followed by a full colon(:),
code to be printed out,
increment/decrement
"""

number = 0
while number < 5:
    print("Hello Moses", number)
    number = number + 1


print('==============================')
# create a python program that prints the even numbers from 50 to 70 using while loop.
number = 50
while number <= 70:
    print(number)
    number = number + 2

print('==============================')
number = 201
while number >= 150:
    print(number)
    number = number - 3