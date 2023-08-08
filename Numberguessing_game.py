# ----------Number3 Guessing game--------------
import random
win_num = random . randint(1,10)
guess=1
game_over= False
while not game_over: 
    guess_num = int(input("Enter your guess b/w 0 and 10:"))
    if win_num==guess_num:
        print(f"YOU WIN  and you guess this number in {guess}th time" )
        game_over=True
    elif  guess_num < win_num:
        print("Too low")
    else:
        print("Too High")
    guess+=1
     

           


