#   ///////  Rock , paper , Scissor  Game ////// 
import random
    
def user_input():
    your_input=input("Enter your choice: 'Rock', 'Paper' , 'Scissor' : ").lower()
    while your_input not in ["rock" ,"paper" , "scissor"]:
        print("Invalid choice !!!!")
        your_input=input("Enter your choice: 'Rock', 'Paper' , 'Scissor' : ").lower()
    return your_input

def comp_input():
    choices =["rock" , "paper" , "scissor"]
    return random.choice(choices)

def winner_selection(user_input,comp_input):
    if user_input==comp_input:
        return "<<<<<<<<TIE!!!!!!>>>>>>"
    elif (user_input == "rock" and comp_input == "scissor") or (user_input == "scissor" and comp_input == "paper") or (user_input == "rock" and comp_input == "paper"):
         return("<<<<<<<<<User Wins!!!!!>>>>>")
    else:
         return("<<<<<COMPUTER WINS!!!!>>>>>")

def main():
    print("///!!!\U0001F600 WELCOME TO 'ROCK' ,'PAPER' ,'SCISSOR' GAME \U0001F600!!!////\n")
    get_user_input=user_input()
    get_comp_input=comp_input()

    print(f"Your Input Is:{get_user_input}\n")
    print(f"Computer Input Is:{get_comp_input}\n")

    Result = winner_selection(get_user_input,get_comp_input)
    print(f"{Result}")

if __name__ == "__main__":
     main()