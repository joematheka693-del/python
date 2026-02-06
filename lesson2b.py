# Tuple
# A tuple is an imutable type of a list (It cannot change)
# To introduce a tuple, we use the paraenthesis ()

counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")

print(counties[3:])

# Accessing items of a tuple by use of the indexes
print(counties[5])

# Note: Below will generate an error
# Attribute error
counties.append("Machakos")
print(counties)