import os
clear = lambda:os.system('cls')
from Blind_Auction_Start.logo import logo

def max_bider(dictoner):
    maxnum=0
    winner=""
    for i in dictoner:
       bid_amount=dictoner[i] 
       if bid_amount> maxnum:
            maxnum=bid_amount
            winner=i
    print(f"The Winner is {winner} with a bid of ${maxnum}.")
        
bids={}
flag=True
while flag!=False:
    print(logo)
    name = input("What is your name ? : ")
    bid = int(input("How much do you bid ? : "))
    bids[name]=bid
    con=input("Anyone else who want to bid ? Yy/Nn : ")
    
    if con=='N' or con=='n':
        max_bider(bids)
        flag=False
    elif con=='Y' or con=='y':
        clear()


