programming_directory={
    "Bug":"An error in a program that prevents the program from running as expected.",
    "Function":"A piece of code that you can easily call over and over again.",
    "Loop":"The action of doing something over and over again."
}
# print(programming_directory)

# Retriving item from the dictionary.
# print(programming_directory["Function"])

# Adding new items to the dictionary.
programming_directory["New"]="This is another new value in dictionary."
# print(programming_directory)

# Create a new empty dictionary.
empty_directory ={}

# wipe an existing dictionary
# programming_directory={}
# print(programming_directory)

# Edit an item in a dictionary
# programming_directory["New"]="Now I edited the value of New."
# print(programming_directory)

# Loop Through a dictionary

for key in programming_directory:
    print(key)
    print(programming_directory[key])