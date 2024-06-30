import random,os
from game_data import data
from art import logo,vs
clear = lambda:os.system('cls')

def get_ran_acc():
    """Get data from random account."""
    return random.choice(data)

def format_data(account):
    """Takes the acc data and returns the printable format."""
    acc_name = account["name"]
    acc_descr = account["description"]
    acc_country = account["country"]
    return f"{acc_name}, a {acc_descr}, from {acc_country}"

def check_ans(Who,a_follow,b_follow):
    """Take the user guess and follower counts and 
    returns True if they got it right.
    Or False if they got it wrong."""
    if a_follow>b_follow:
        return Who=="a"
    else:
        return Who=="b"
clear()
def game():
    # Display Art 
    print(logo)


    flag=True
    score=0
    account_b = get_ran_acc()

    # Loop repeating till user guess wrong !!
    while flag:
        
        account_a = account_b
        account_b = get_ran_acc()
        while account_a == account_b:
            account_b = get_ran_acc()

        print(f"Compare A: {format_data(account_a)}.")
        #print(account_a["follower_count"])
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        #print(account_b["follower_count"])
        WhoHas=input("Who has more followers? Type 'A' or 'B': ").lower()

        # Check if user is correct.
        # Get followers count of each account.
        followersA=account_a["follower_count"]
        followersB=account_b["follower_count"]
        iscorrect=check_ans(WhoHas,followersA,followersB)
        
        clear()
        print(logo)
        # Give user feedback on their guess.
        if iscorrect:
            score+=1
            print(f"You're right! Currect score: {score}.")

        else:
            flag = False
            print(f"Sorry,that's wrong. Final score: {score}")

game()
    