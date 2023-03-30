#This game is Rock, Paper and Scissors

import random, sys
print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True: #This main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: #The player input loop
        playerMove = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit\n')
        if playerMove == 'q':
            sys.exit() #Quit the program.

        if playerMove == 'r' or playerMove == 'p' or playerMove =='s':
            break #Break out of the player input loop
        print('Type one of r, p, s, or q.')
    
    #Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus....')
    elif playerMove == 'p':
        print('PAPER versus....')
    elif playerMove == 's':
        print('SCISSORS versus...')

    #Display what the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        compMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        compMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        compMove = 's'
        print('SCISSORS')
# Display and record the win/loss/tie:
    if playerMove == compMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and compMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and compMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and compMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and compMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and compMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and compMove == 'r':
        print('You lose!')
        losses = losses + 1
    