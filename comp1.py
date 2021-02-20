import random
print("......rock......")
print("......paper......")
print("......scisscors.....")

player = input("enter your move : ").lower()
num = random.randint(0,2)
if num == 0:
    computer = "rock"
    print(f"computer plays {computer}")
elif num == 1:
    computer = "paper"
    print(f"computer plays {computer}")
else:
    computer = "scissors"
    print(f"computer plays {computer}")

if player == computer:
    print("its a tie")
elif player == "rock":
    if computer == "paper":
        print("computer is winner")
    elif computer == "scissors":
        print("you won")
elif player == "paper":
    if computer == "rock":
        print("you won")
    elif computer == "scissors":
        print("computer wins")
elif player == "scissors":
    if computer == "rock":
        print("computer is winner")
    elif computer == "paper":
        print("you win")
else:
    print("make right choice")

