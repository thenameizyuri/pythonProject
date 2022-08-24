# Nobel CS CluB
import random


def snake_water_gun(robot, you_user):
    if robot == you_user:
        return None
    elif robot == 's':
        if you_user == 'w':
            return False
        elif you_user == 'g':
            return True
    elif robot == "w":
        if you_user == 's':
            return True
        elif you_user == 'g':
            return False
    elif robot == 'g':
        if you_user == 's':
            return False
        elif you_user == 'w':
            return True


print("Computer choose the option among snake, water and gun\n")
randomnumber = random.randint(2,4)

if randomnumber == 2:
    robot = 's'
elif randomnumber == 3:
    robot = 'w'
elif randomnumber == 4:
    robot = 'g'

you_user= input("Now its your turn : choose 's' for snake and 'w' for water and 'g' for gun\n")

print('Computer choose '+(robot))
print('You choose ' + (you_user))

bool = snake_water_gun(robot, you_user)

if bool == None:
    print("The game is Tie")
elif bool == True:
    print("you win the game")
else:
    print("you lose the game")
