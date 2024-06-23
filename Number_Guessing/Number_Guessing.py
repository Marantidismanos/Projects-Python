import random,os
from logo import logo1,logo2

RandomNum=random.randint(1,100)
Easy_tries=10
Hard_tries=5

def guess(user):
        if user==RandomNum:
            print(f"You find the number,you Win. The nunber was{RandomNum}!!! ")
            return 0
        elif user>RandomNum:
            print("Too High !")
        else:
            print("Too Low !")

def difficulty():
    dif=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if dif=='easy':
        print("You have 10 attempts remaining to guess the number.")
        return Easy_tries
        
    else:
        print("You have 5 attempts remaining to guess the number.")
        return Hard_tries
        

def game():
    print(logo1)
    print("Welcome to the Number Guessing Game !!")
    print("I'm thinking of a number between 1 and 100.")
    
    tries=difficulty()

    for i in range(tries):
        user=int(input("Make a guess: "))
        gue=guess(user)
        if gue==0:
            break;
        print(f"{tries-i-1} Tries remaining to guess the number !")
    print("You didn't find the number,you Lose !")
    print(logo2)

game()