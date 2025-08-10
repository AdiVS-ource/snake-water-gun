import random
from colorama import Fore ,Style,init
init(autoreset=True)

youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "snake", -1: "water", 0: "gun"}


score = {"You": 0, "Computer": 0, "Draws": 0}

def print_score():
    print(f"\n {Fore.YELLOW} Scoreboard")
    for player, points in score.items():
        print(f"{player}:{points}")
    print()

print(f"{Fore.CYAN}=== Welcome to Snake-Water-Gun Game ===")
print(f"{Fore.MAGENTA}Rules:")
print(" Snake drinks Water → Snake wins")
print(" Water damages Gun → Water wins")
print(" Gun shoots Snake → Gun wins\n")
print("Controls: s = Snake, w = Water, g = Gun, q = Quit")

while True:
     computer = random.choice([-1,0,1])
     youstr = input(f"{Fore.CYAN}enter your choice : ").lower()

     if youstr == "q":
        print(f"\n{Fore.GREEN}Thanks for playing!")
        print_score()
        break

     if youstr not in youdict:
        print(f"{Fore.RED}Invalid choice! Try again.")
        continue

     you = youdict[youstr]
     print(f"You chose { Fore.BLUE} {reversedict[you]}{Style.RESET_ALL} and computer chose{Fore.BLUE} {reversedict[computer]} ")

     if you == computer:
       print(f"{Fore.YELLOW}its a draw")
       score["Draws"]+=1

     elif(you==1 and computer ==-1) or\
      (you==0 and computer ==1) or\
      (you==-1 and computer ==0) :
         print(f"{Fore.GREEN} You win this round !")
         score["You"]+=1

     else:
        print( f"{Fore.RED} You lost this round")
        score["Computer"]+=1

     print_score()
