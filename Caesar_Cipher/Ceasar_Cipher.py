from Blind_Auction_Start.logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z']

def caesar(direction,texted,shifted):
        end_text=""
        if direction=="decode":
            shifted*= -1
        for i in texted:
            if i in alphabet:
                position = alphabet.index(i)
                new_position = (position + shifted) 
                end_text += alphabet[new_position]
            else:
                end_text += i       
        print(f"The {direction} Text is : {end_text}.")    
        
            
print(logo)
flag=True

while flag!=False:
    flagin=True
    
    while flagin!=False:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction=='encode' or direction=='decode':
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            shift = shift % 26
            caesar(direction,text,shift)
            flagin=False
        else:
            print("You didnt choose encode or decode !!!")
            flagin=True
    flagcon=True

    while flagcon!=False:
        con= input("You want to continue? Yy/Nn : ")
        if con=='Y' or con=='y':
            flag=True
            flagcon=False
        elif con=='N' or con=='n':
            flag=False
            flagcon=False
            print("Goodbye")