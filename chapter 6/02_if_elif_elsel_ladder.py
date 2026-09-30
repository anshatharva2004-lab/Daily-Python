a = int(input("enter your age:"))

#if elif else ladder

if(a>=18):
    print("you are above age consent")
    print("you are not good to go")
elif(a<0):
    print("not possible")
elif(a==0):
    print("invalid age")        
else:print("you are under the age consent")

print("end of program")