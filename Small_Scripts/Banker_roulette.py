import random

names=['angela' ,'ben', 'jenny', 'michael', 'chloe']
num_items=len(names)

random_choice=random.randint(0,num_items-1)
print(names[random_choice]," is going to buy meal today")