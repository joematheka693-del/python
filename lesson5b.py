# Functions with parameters
# They are values that get passed as arguments given to a function inside of the parenthesis.


def greeting(name):
    print(f"{name} How are you? Hope everything is fine.")

greeting("Matheka")
greeting("June")
greeting("Prince")

print("==============================================")
def message(names):
    print(f"Hello {names}. We shall be having a general meeting on date..... Please avail Yourself.")

message("Joe")
message("Yvonne")

print("=========================================")
# Create a function that accepts parameters to add two numbers.
def addition(a, b):
    sum = a + b
    print("The sum of the number is, ", sum)

addition(20, 30)
addition(40, 90)