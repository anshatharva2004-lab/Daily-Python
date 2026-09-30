def grestest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    elif(c>a and c>b):
        return c

a =58
b= 84
c=100
print(grestest(a,b,c))    