import random 


# logic
def gameWin(comp,user):
    if comp == user:
        return None
    elif comp == 's':
        if user == 'g':
            return True
        elif user == 'w':
            return False
    elif comp == 'w':
        if user == 's':
            return True
        elif user == 'g':
            return False
    elif comp == 'g':
        if user == 'w':
            return True
        elif user == 's':
            return False

# computer output
print("Comp Turn: snake(s),water(w),gun(g):")
randNo =random.randint(1,3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

# input
user = input("Your Turn!Enter snake(s),water(w),gun(g):= ")
a = gameWin(comp,user)

print(f"Computer chose {comp}")
print(f"You chose {user}")

# out result
if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")