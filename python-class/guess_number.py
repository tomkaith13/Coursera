# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import math
import random

# initialize global variables used in your code
secret_no=0
range=1
player_guess=0
chances=0
max_chance=0



# helper function to start and restart the game
def new_game():
    global secret_no, range, player_guess, chances, max_chance
    player_guess=0
    chances = 0    
    
    if range == 1:
        print '==========================================='
        print '\n\nThe secret number is in the range [0-100)'
        print 'Enter your guess in the input field '
        secret_no = random.randrange(0,100)
        max_chance=math.ceil((math.log((100 - 0 + 1)))/math.log(2))
    else:
        print '\n\nThe secret number is in the range [0-1000)'
        print 'Enter your guess in the input field'
        secret_no = random.randrange(0,1000)
        max_chance=math.ceil((math.log((1000 - 0 + 1)))/math.log(2))
    chances=int(max_chance)
    print 'You have max of ',chances,' chances\n'
   


# define event handlers for control panel
def range100():
    global range
    range = 1
    new_game()

def range1000():
    global range
    range=2
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global player_guess, secret_no, chances
    win=0
    player_guess = int(guess)
    print 'Your guess is:',player_guess
    
    
    if player_guess < secret_no:
        print 'Computer says guess Higher'
    elif player_guess > secret_no:
        print 'Computer says guess Lower'
    else:
        print 'You guessed it right!! You win !!'
        win=1
        new_game()
            
    if win != 1:
        # decrement only if we did not win yet
        chances = chances - 1
        print 'you have ',chances,' chances left\n'
        
    if chances == 0:        
        # your chances are over
        print 'You did not guess in ', int(max_chance),' guesses'
        print 'the secret number was:',secret_no
        print ' You lose!!\nTry again!'
        new_game()

# create frame
f = simplegui.create_frame('Guess the number', 200, 200)




# register event handlers for control elements
button_range1=f.add_button('Range [0 - 100)', range100)
button_range2=f.add_button('Range [0 - 1000)', range1000)
inp_guess=f.add_input('Player guess',input_guess,100)


# call new_game and start frame
new_game()
f.start()


# always remember to check your completed program against the grading rubric
