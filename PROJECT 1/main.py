''' water = -1
snake = 1
gun = 0'''
import random
computer = random.choice([-1,1,0])
yourtr = input("enter you choice: ")
yourdict = {"s": 1, "w":-1,"g":0}
reversdict = {1:"snake", -1:"snake", 0:"water"}

you = yourdict[yourtr]

# by now we have 2 number(variables), you and computer

print(f" you choose  {reversdict[you]}\n computer  {reversdict[computer]} ")

if(you == computer):
    print(" it's a draw")
else:
    if(computer == 0 and you == 1):
        print(" you lose")
    elif(computer == 0 and you == -1):
            print(" you win")
    elif(computer == 1 and you == -1):
            print(" you lose")
    elif(computer == 1 and you == 0):
            print(" you win")
    elif(computer == -1 and you == 1):
            print(" you win")
    elif(computer == -1 and you == 0):
            print(" you win")
    else:
           print("something went wrong")        


# additionl analysis/ here instad of using many lins , i uesd mu own logic to make code shorter
# not an idol method and not readable
if ((computer - you) == -1 or (computer - you) ==2 ):
       print("you lose")
else:
       print("you win")                 
    