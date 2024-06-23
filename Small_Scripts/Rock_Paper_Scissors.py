import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices=[rock,paper,scissors]
user=int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors. : \n"))
com=random.randint(0,2)
if user>=3 or user<0:
    print("You typed an invalid number you lose !!")

else:
    print("You chose : \n")
    print(choices[user])

    print("Computer chose: \n")
    print(choices[com])

    if user==0 and com==2:
        print("You Win !")
    elif com==0 and user==2:
        print("You lose !")
    elif com > user:
        print("You lose !")
    elif user > com:
        print("You Win !")
    elif com==user:
        print("Tie !!")

'''''
if user==0 and com==2:
    print("You Win !")
elif user==0 and com==1:
    print("You lose !")
elif user==0 and com==0:
    print("Tie !!")
elif user==1 and com==0:
    print("You Win !")
elif user==1 and com==2:
    print("You lose !")
elif user==1 and com==1:
    print("Tie !!")
elif user==2 and com==1:
    print("You Win !")
elif user==2 and com==0:
    print("You lose !")
elif user==2 and com==2:
    print("Tie !!")
else:
    print("You typed an invalid number you lose !!")
'''''

