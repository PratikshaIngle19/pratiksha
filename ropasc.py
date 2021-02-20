print("......rock......")
print("......paper......")
print("......scisscors.....")

ply1 = input("ply1, make your move ")
ply2 = input("ply2, make your move ")

if ply1 == "rock" and ply2 == "paper":
    print("ply2 is winner")
elif ply1 == "rock" and ply2 == "scisscors":
    print("ply1 is winner")
elif ply1 == "paper" and ply2 == "rock":
    print("ply1 is winner")
elif ply1 == "paper" and ply2 == "scisscors":
    print("ply2 is winner")
elif ply1 == "scisscors" and ply2 == "rock":
    print("ply2 is winner")
elif ply1 == "scisscors" and ply2 == "paper":
    print("ply1 is winner")
elif ply1 == ply2:
    print("its tie")
elif ply1 == "":
    print("make right move ply1")
elif ply2 == "":
    print("make right move ply2")
else:
     print("something went wrong")