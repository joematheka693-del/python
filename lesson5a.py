# Python Functions
# They are a block of code/statements that performs a given task/action. They can be reused throughout the program to perform different tasks.
# Functions are defined using the def keyword. (define)
# We have two main types of functions i.e:
# 1. In built functions -> They come preinstalled with the interpreter i.e print(), pop(), range(), append(), etc...
# 2. User defined functions => They are created by a programmer to solve a iven task.
# To define a function you need to give it a name followed by a parenthesis.
# For the functions, it is usually indented and to invoke a function we use the function name.


def greetings():
    print("Hello, how are you?")


# Below we call the function by ise of its name
greetings()

print("================================================================")

# Addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is: ", sum)

addition()

print("================================================================")
# Create a function that is able to multiply three values

def multiplication():
    num3 = 20
    num4 = 50
    num5 = 6
    product = num3 * num4 * num5
    print("The product of the three numbers is: ", product)

multiplication()

print("======================================")
# Below is a division function
def divide():
    number1 = int(input("Enter the first number"))
    number2 = int(input("Enter the second number"))
    quotient = number1 / number2
    print("THe answer is: ", quotient)

divide()

for function in range(2):
    divide()
