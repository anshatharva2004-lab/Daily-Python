n = int(input("enter the number:"))
for i in range(1, n+1):
    print(" "* (n-1), end="")
    print("*"* i, end="")
    print("")