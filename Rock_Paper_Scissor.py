"""

WORK FLOW OF PROJECT:
1 - INPUT FROM USER(ROCK , PAPER , SCISSOR)
2 - COMPUTER CHOICE (COMPUTER WILL CHOOSE RANDOMLY NOT CONDITIONALLY)
3 - RESULT PRINT

CASES:

A- ROCK 
ROCK -ROCK  = TIE 
ROCK - PEPAR = PAPER WIN 
ROCK - SCISSOR = SCISSOR WIN 

B-PAPER
PAPER - ROCK = ROCK  WIN 
PAPER - PAPER  = TIE
PAPER - SCISSOR = SCISSOR WIN 

C-SCISSOR
SCISSOR - ROCK = ROCK WIN
SCISSOR - PAPER = SCISSOR WIN
SCISSOR - SCISSOR = TIE

"""
import random
print("***WELLCOME TO THE GAME ROCK_PAPER_SCISSOR***\n")
List_Item = ["ROCK","PAPER","SCISSOR"]

User_Choice = input("Enter your move(ROCK,PAPER,SCISSOR) =  ")
Computer_Choice = random.choice(List_Item)

print(f"User choice = {User_Choice}")
print(f"Computer_Choice= {Computer_Choice}")

if User_Choice == Computer_Choice:
    print("Both chooses same  , Match Tie")

elif User_Choice ==  "ROCK":
    if Computer_Choice == "PAPER":
        print("paper coves rock  ,  computer win")
    else :
        print("Rock smashes Scissor ,  you win")   

elif User_Choice == "PAPER":
    if Computer_Choice == "SCISSOR":
        print("Scissor cuts paper , computer win")
    else:
        print("paper coves rock , you win")
        
elif User_Choice == "SCISSOR":
    if  Computer_Choice == "PAPER":
        print("Scissor cuts paper , you win")
    else:
        print("Rock smashes Scissor , computer win ")
        
print("GAME_OVER")        
                 