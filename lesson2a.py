# Python lists
# A list in python is a collection of iems that ordered in a certain way.
# A list is introduced by the use of the square brackets [].
# The items of lists are stored inside of indexes. Note: In programmin we start counting from index zero(0). BMW, Mercedes, Lamborghini, ...
# A list is mutable i.e the contents of a list can be changed.

cars = ["BMW", "Mercedes", "Lamborghini", "Ferari", "Mustang", "McLarren", "Tesla"]

print(cars)
print(type(cars))

# Accessing items of a list.
print(cars[2])
print("The car on index four is: ", cars[4])


# List slicing - This is creating list from a given bigger list.
print(cars[4:])

# Printing from index zero to index three.
print(cars[:4])

# Print Lamborghini to Mustang
print(cars[2:5])

# List - Mutability
# We use the function append to add an item at the end of a list.
cars.append("Toyota")
print(cars)

cars.append("Subaru")
print(cars)

# We use the pop function to remove an itm at the end of the list.
cars.pop()
print(cars)

# We can use an index to add items to a list.
cars[5] = "Pajero"
print(cars)

# We can use the sort function to sort out items in alphabetical order.
cars.sort()
print(cars)
