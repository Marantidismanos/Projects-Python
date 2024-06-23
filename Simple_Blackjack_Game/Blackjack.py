import random,os
clear= lambda: os.system('cls')
from logo import logo

def deal_card():
    """ Returns a random card from the deck. """
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(userscore,comscore):
    if userscore == comscore:
        return "Draw !!!"
    elif comscore==0:
        return "Lose,oppenent has Blackjack 😭!!!"
    elif userscore==0:
        return "Win with a Blackjack 😎!!!"
    elif userscore > 21:
        return "You went over. You lose 😭!!!"
    elif comscore > 21:
        return "Opponent went over, You win 😎!!!" 
    elif userscore > comscore:
        return "You win 😎!!!"
    else:
        return "You lose 🤯!!!"
    
def Blackjack():
    print(logo)
    user_cards=[]
    computer_cards=[]
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        score_user=calculate_score(user_cards)
        score_com=calculate_score(computer_cards)
        print(f"Your cards {user_cards} ,current score : {score_user}")
        print(f" Computer's first card: {computer_cards[0]}")

        if score_user==0 or score_com==0 or score_user>21:
            is_game_over=True
        else:
            con=input("Type 'y' to get another card,type 'n' to pass: ")
            if con=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True
    while score_com!=0 and score_com < 17:
        computer_cards.append(deal_card())
        score_com=calculate_score(computer_cards)

    print(f" Your final hand: {user_cards},final score: {score_user}.")
    print(f" Computer's final hand: {computer_cards},final score: {score_com}.")
    print(compare(score_user,score_com))

while input("Do you want to play Blackjack ? 'y' or 'n' ") == "y":
    clear()
    Blackjack()

print("Goodbye !!!")