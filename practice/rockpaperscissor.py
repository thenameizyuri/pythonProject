# Nobel Cs cluB
import random

def rock_paper_scissor(you, computer):

    if computer == you:
        return None
    elif computer == 'Rock':
        if you == 'Paper':
            return True
        elif you == 'Scissor':
            return False
    elif computer == 'Paper':
        if you == 'Rock':
            return False
        elif you == 'Scissor':
            return True
    elif computer == 'Scissor':
        if you == 'Rock':
            return True
        elif you == 'Paper':
            return False


you_score = 0
computer_score = 0
computer = None
while True:
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
        print(f'Computer : {computer_score}')
        print(f'You : {you_score}')
        break

    print(f'You choose {you}')
    print(f'Computer choose {computer}')

    gameWin = rock_paper_scissor(you, computer)

    if gameWin == None:
        print("The game is Tie \n")
    elif gameWin == True:
        you_score += 1
        print("You win the game \n")
    else:
        computer_score += 1
        print('YOu lose the game \n')

