import os

directory = "/chapter 1 ps sheet"
contents = os.listdir(directory)

for item in contents:
    print(item)