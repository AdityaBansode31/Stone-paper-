from operator import truediv
import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'c':
            return False
        elif you == 'p':
            return True
    elif comp == 'p':
        if you == 's':
            return False
        elif you == 'c':
            return True
    elif comp == 'c':
        if you == 'p':
            return False
        elif you == 's':
            return True

print("computer's turn: Stone(s) Paper(p) Scissors(c) ??")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'c' 
you = input("player's turn: Stone(s) Paper(p) Scissors(c) ??")

a = game(comp, you)

if a == None:
    print("The game is tied!!")
elif a:
    print("YOu Won!!")
else:
    print("You lost")

print("you choose:" + you)
print("opponent choose:" +comp)
