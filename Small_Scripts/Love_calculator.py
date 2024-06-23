print("The love calc is calculating your score...")


name1=input("What is your name ?")
name2=input("What is their name ?")
bothnames=name1+name2
lnames=bothnames.lower()


t=lnames.count("t")
r=lnames.count("r")
u=lnames.count("u")
e=lnames.count("e")
fnum=t+r+u+e
l=lnames.count("l")
o=lnames.count("o")
v=lnames.count("v")
e=lnames.count("e")
snum=l+o+v+e
score=int(str(fnum)+str(snum))
if score<10 or score>90:
    print(f"Your score is {score} ,you go together like coke and mentos !")
elif score>=40 and score<=50:
    print(f"Your score is {score} ,you go alright together!")
else:
    print(f"Your score is {score}.")