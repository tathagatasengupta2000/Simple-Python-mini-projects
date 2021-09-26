from os import system
#HINT: You can call clear() to clear the output in the console.
from art1 import logo
print(logo)
Bidders="Yes"
dict={}
def Declear():
    Win=0
    system('cls')
    for key in dict:
        Bid=int(dict[key])
        if Bid>Win:
            Win = Bid
            Name=key
    print(f"{Name} Has Bidded {Win} and has WON the Bidding ")
while True:
    name=input("Please Enter Your Name: ")
    bid=input("Please Enter Your Bid: $")
    dict[name]=bid
    Bidders=input("Are There any other Bidders YES/NO ")
    if Bidders=="YES":
        system('cls')
    if Bidders=="NO":
        break
Declear()

