import random
random_num = random.randint(1,10)
while True:
    choice = int(input("Guess the number : "))
    if choice >random_num:
        print("you are too high")
    elif choice < random_num:
        print("you are too low")
    else:
        print("you are correct")
        j = input("do you want to continue (y \ n) : ")
        if j == "y":
            random_num = random.randint(1,10)
        else:
            print("thanks for playing")     
            break

