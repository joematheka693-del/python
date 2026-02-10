# A for loop can also be used to iterate through a list, tuple, string or a dictionary...

name = "Matheka"

for letter in name:
    if letter == "h":
        print("This is letter h")
    else:
        print(letter)

print("==============================================================================")
# Below is a list of counties.
counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]

print(counties)

for county in counties:
    print(county)

print("===========================================================================")

if "Machakos" in counties:
    print("This is in the list of counties")
else:
    print("This is not in the list of counties")

print("=======================================================================")

for county in counties:
    if "Nairobi" in counties:
        print("The county is part of the list")
else:
    print("The county is not part of the list")

print("===================================================================")
# The for loop can also be used to iterate through a dictionary



player = {
    "name" : "Mbappe",
    "age" : 25,
    "teams" : ["PSG", "Monaco", "France"],
    "nationality" : "French"
}

for key in player:
    print(key)
print("======================================================")
for x in player:
    print(player[x])

print("=====================================================================")
# Loop through the teams the player kas player for.
for x in player["teams"]:
    print(x)