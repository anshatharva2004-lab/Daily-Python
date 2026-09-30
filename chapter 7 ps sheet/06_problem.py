n = int(input("enter the number:"))
product= 1 #intialize product from 1 
for i in range(1,n+1): #aga sirf n karte toh n-1 tak jata
    product = product*i
    print(f"the factorial of {n} is {product}")
