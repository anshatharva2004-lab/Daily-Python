import os

# Path of the directory
directory = "/chapter 1 ps sheet"

# Get the contents of the directory
contents = os.listdir(directory)

# Print each item
for item in contents:
    print(item)