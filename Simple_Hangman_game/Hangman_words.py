import random ,os
clear= lambda: os.system('cls')

from Hangman_art import stages,logo
from Hangman_words_list import word_list


chosen_word=random.choice(word_list)
word_lenght=len(chosen_word)
blanklist=[]
endgame=False
lives=6
for i in range(word_lenght):
    blanklist+="_"
win_lose=["You win !!","You lose !!"]
flag=0

print(logo)


print(f"The word start with ~~~~~>{chosen_word[0]}<~~~~,")
print(f"and the lenght of word in letters is {word_lenght}")
while not endgame:    
    user=input("Guess a letter : ").lower()
    clear()
    
    if user in blanklist:
        print(f"You've already guessed {user}")

    for i in range(word_lenght):
        letter=chosen_word[i]
        if letter == user:
            blanklist[i]=letter
    if user not in chosen_word:
        print("The letter that you chose ,isn't in the word !!")
        print("You lose a live !!")
        lives-=1
        if lives==0:
            endgame=True
            flag=2                            
    if "_" not in blanklist:
        endgame=True
        flag=1
    print("Lives left : ",lives)       
    print(stages[lives])  
    print(blanklist)
    
if flag==1:
    print(win_lose[0])
else:
    print(win_lose[1])
  
#Join all the elements in the list and turn it into a String.   
print(f"The word was : {' '.join(chosen_word)}")
    
        

        


    
    


