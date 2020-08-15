# Guided Exploration No. 3
# Rosalie Roberts
# Theme and file names revised to be entertaining but avoid cultural appropriation

# This imports a random number
import random

# This is an empty variable that will store the possible names
possible_names = []

# This will stores the names in a file
outputFile = open('klezmer-names-output.txt', 'w')

# This opens the file titled 'klezmer-names" and uses the data (the list of names and whatnot)
with open('klezmer-names.txt', 'r') as dataFile:
    # This iterates through the names and assigns it to the variable name
    for name in dataFile:
        # this strips off the invisible line feed and appends lines with names from the list at random
        possible_names.append(name.rstrip())


# This asks the user how many klezmer names they want to create and counts them for use in the iterator
count = int(input('How many klemzer names would you like to create? '))
# This asks the user how many parts or possible names from the file will go in the name
parts = int(input('How many parts should the name contain? '))

# This uses the amount of names specified by the user to iterate through the loop that many times
for i in range(count):
    # This creates a variable name parts in which to store the names
    name_parts = []
    # This uses the number of parts specified by the user to iterature though the loop that many times
    for j in range(parts):
        # this appends or adds to the counted loop the name that is randomly generated through the file
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

# This stores the above in a file
outputFile.write(f"{' '.join(name_parts)}\n")
# This displays what is stored in the file
print(f"{' '.join(name_parts)}")
