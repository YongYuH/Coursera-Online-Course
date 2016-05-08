# Rock-paper-scissors-lizard-Spock template
'''
http://www.codeskulptor.org/#user40_JRv9xyaKeyRS4Zs.py
'''

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if(name == "Rock" or name == "rock"):
        number = 0
        return number
    elif(name == "Spock" or name == "spock"):
        number = 1
        return number
    elif(name == "Paper" or name == "paper"):
        number = 2
        return number
    elif(name == "Lizard" or name == "lizard"):
        number = 3
        return number
    elif(name == "Scissors" or name == "scissors"):
        number = 4
        return number
    else:
        print "Wrong input!"
                
def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if(number == 0):
        name = "rock"
        return name
    elif(number == 1):
        name = "Spock"
        return name
    elif(number == 2):
        name = "paper"
        return name
    elif(number == 3):
        name = "lizard"
        return name
    elif(number == 4):
        name = "scissors"
        return name
    else:
        print "Wrong input! Please enter a non-negative integer between 0 to 4."
               
import random
    
def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player chooses", player_choice 
    # convert the player's choice to player_number using the function name_to_number()
    number_of_player_choice = name_to_number(player_choice)
    if(number_of_player_choice != None):
        # compute random guess for comp_number using random.randrange()
        number_of_computer_choice = random.randrange(0, 4)
        # convert comp_number to comp_choice using the function number_to_name()
        computer_choice = number_to_name(number_of_computer_choice)
        # print out the message for computer's choice
        print "Computer chooses", computer_choice
        # compute difference of comp_number and player_number modulo five  
        number_of_result = number_of_player_choice - number_of_computer_choice
        number_of_result %= 5   
        # use if/elif/else to determine winner, print winner message
        if(number_of_result == 0):
            print "Player and computer tie!"
        elif(number_of_result >= 2):
            print "Computer wins!"
        else:
            print "Player wins!"
    else:
        print "Please enter one of Rock-paper-scissors-lizard-Spock."
        
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("scissor")

# always remember to check your completed program against the grading rubric