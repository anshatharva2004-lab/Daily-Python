f = open("file.text")
print(f.read())
f.close()


#the same ststement can in single line using with ststement
with open("file.text") as f:
    print(f.read())


#you don't have to explicitly close the file when using with statement, it will automatically close the file after the block of code is executed.