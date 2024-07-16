import random
#         GENERATING RANDAM INTEGER
target = random.randint(1 , 100)

while True:
    userChoice = (input("Guess the target or Quit(Quit) :"))
    if(userChoice == "Quit"):
        break
    
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number was too small. Take a bigger guess....")
    else:
        print("your number was too large. Take a smaller guess....")

    
print("_____GAME OVER____")    
