#First game is rock paper scissors 
from random import randint 

def random_response(): 
    pass

print("Lets play rock paper scissors!")

user_i = input("Pick: r for rock, p for paper and s for scissors!")

while user_i: 
    if user_i.lower() == "r": 
       if random_response() != "scissors":
           print("You lost!!!")
       else: 
           print("You won!!!")
           break
    play_again = input("Would you like to play again? (yes/no)")
    

