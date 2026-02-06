# A dictionary is a data type that stores data in terms of key - value pair.
# It is introduced by the use of curly braces {}
# The values stored inide of a dictionary can be of any data type.
# To access the valies in a dictionary we use the keys


phonebook = {
    "Benson" : "+2547387098",
    "Mary"  : "+25478789877",
    "Stephen" : "+25478876265"
}

# Showing the entire dictionary
print(phonebook)
print(type(phonebook))

print(phonebook["Benson"])

print('================================')


player = {
    "name" : "Messi",
    "Age" : 40,
    "Teams" : ["PSG", "Barcelona", "Argentina"],
    "more" : {
        "children" : 3,
        "residence" : "US",
        "phone" : (2547788993, 2548989879, 2548778990)
    }
}

print(player["Teams"][1])

# print messi second number
print(player["more"]["phone"][1])
