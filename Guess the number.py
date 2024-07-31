import random
target=random.randint(1,100)
while True:
    user_choice=input("Guess the target or Quit(Q):")

    if(user_choice=="Q"):
        break
    user_choice=int(user_choice)
    if(user_choice == target):
        print("Success : Correct Guess!!")
        break
    elif(user_choice<target):
        print("your number was too small, take a bigger guess")
    else:
        print("your number was too big, take a smaller guess")
print("----Game Over----")
