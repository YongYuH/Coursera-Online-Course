# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# For user interface
import simplegui

# For creating random variable
import random

# For using log function to decide the maximun times user can enter
import math

secret_number = 0
Maximun_number = 100
Maximun_try_times = 7
guess_num = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here    
    global secret_number
    global Maximun_try_times   
    secret_number = random.randrange(0, Maximun_number)
    print "New game! The range is from", 0, "to", Maximun_number
    
    # Vary the number of allowed guesses based on the range of the secret number
    Maximun_try_times = int(math.ceil(math.log(Maximun_number - 0 + 1, 2)))
    print "You can try", Maximun_try_times, "times"    
    print ""    
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global Maximun_number
    Maximun_number = 100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global Maximun_number
    Maximun_number = 1000
    new_game()
    
def input_guess(guess):
    global Maximun_try_times
    global guess_num
    # avoid error when user does not enter an integer
    try:
        guess_num = int(guess)             	           
        print "Guess was", guess_num
        Maximun_try_times -= 1
        # main game logic goes here
        if (Maximun_try_times != 0): 
            print "You can still try", Maximun_try_times, "times"    
            if (secret_number == guess_num):
                print "Correct"
                print ""       
            elif (secret_number < guess_num):
                print "Lower"
                print ""      
            elif (secret_number > guess_num):
                print "Higher"
                print ""       
            else:
                print "Error when comparing the secret number and the guess number!"
                print ""        
        else:
            print "Sorry! You have used all the chance!"
            print ""
            print "The game would restart immediately!"
            print ""
            new_game() 
    except ValueError:
        print "You have enter", guess
        print "That is not an integer number!"
        Maximun_try_times -= 1
        if (Maximun_try_times != 0): 
            print "You can still try", Maximun_try_times, "times" 
            print ""
        else:
            print "Sorry! You have used all the chance!"
            print ""
            print "The game will restart immediately!"
            print ""
            new_game()
            
# create frame
frame = simplegui.create_frame("Guess the number", 300, 300)

# register event handlers for control elements and start frame
range100_button = frame.add_button("Range is [0, 100)", range100)
range1000_button = frame.add_button("Range is [0, 1000)", range1000)
input_text = frame.add_input("Enter a guess number", input_guess, 100) 

# call new_game 
frame.start()
new_game()

# always remember to check your completed program against the grading rubric