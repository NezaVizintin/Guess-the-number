import random
import simplegui

# global variables
secret_number = 0
upper_range = 100
tries = 7

# helper function to start and restart the game
def new_game(upper_range):
    global secret_number, tries
    secret_number = random.randrange(0, upper_range)
    if upper_range == 1000:
        tries = 10
    else:
        tries = 7
    print('New game! Guess the number between 0 and (not including) ' + str(upper_range))
    print 'Number of guesses left: ' + str(tries)
    print''

# define event handlers for control panel
def range100():
    global upper_range, tries
    upper_range = 100
    new_game(upper_range)
    
def range1000():
    global upper_range, tries
    upper_range = 1000
    new_game(upper_range)
    
def input_guess(string_guess):
    # prints out what the player guessed
   
    print('Guess was ' + string_guess)
    global tries
    tries -= 1
    print 'Number of guesses left: ' + str(tries)
    
    float_guess = float(string_guess)
    
    if float_guess == secret_number:
        print('Correct')
        print ''
        new_game(upper_range)

    elif float_guess < secret_number:
        print('Higher')
        print ''
    else:
        print('Lower')
        print ''
   
    if tries == 0:
        new_game(upper_range)
       
# create frame
frame = simplegui.create_frame('Testing', 100, 200)
inp = frame.add_input('Guess', input_guess, 50)

# register event handlers for control elements and start frame

button_100 = frame.add_button('Range is [0, 100)', range100)
button_1000 = frame.add_button('Range is [0, 1000)', range1000)

# call new_game 
new_game(upper_range)
