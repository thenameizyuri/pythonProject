# Nobel Cs cluB
import random

def rock_paper_scissor(you, computer):
    if computer == you :
        return None
    elif computer == 'Rock':
        if you == 'Paper':
            you_score =+1
            return True
        elif you == 'Scissor':
            cpu_score =+1
            return False
    elif computer == 'Paper':
        if you == 'Rock':
            cpu_score =+1
            return False
        elif you == 'Scissor':
            you_score =+1
            return True
    elif computer == 'Scissor':
        if you == 'Rock':
            you_score =+1
            return True
        elif you == 'Paper':
            cpu_score =+1
            return False



while True:
    cpu_score = 0
    you_score = 0

    print('Rock, Paper or Scissor ?')
    print('Computer : I choose and its Ur turn :')
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computer = 'Rock'
    elif randomNumber == 2:
        computer = 'Paper'
    elif randomNumber == 3:
        computer = 'Scissor'

    print("Rock, Paper , Scissor ?")
    you = input("User : \n").capitalize()
    if you == 'End':
        print('Game Scores:\n')
        print(f'Computer : {cpu_score}')
        print(f'You : {you_score}')
        break

    print(f'You choose {you}')
    print(f'Computer choose {computer}')

    gameWin = rock_paper_scissor(you, computer)

    if gameWin == None:
        print("The game is Tie \n")
    elif gameWin == True:
        print("You win the game \n")
    else:
        print('YOu lose the game \n')
