#this is not mine but gpt code


import random

computer = random.choice([-1, 1, 0])

yourtr = input("Enter your choice (s/w/g): ")

yourdict = {"s": 1, "w": -1, "g": 0}
reversdict = {1: "snake", -1: "water", 0: "gun"}

you = yourdict[yourtr]

print(f"You chose {reversdict[you]}")
print(f"Computer chose {reversdict[computer]}")

if you == computer:
    print("It's a draw")

elif (you == 1 and computer == -1) or \
     (you == -1 and computer == 0) or \
     (you == 0 and computer == 1):
    print("You win")

else:
    print("You lose")
