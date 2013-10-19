# Rock-paper-scissors-lizard-Spock template


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
import random
def number_to_name(number):
    # fill in your code below    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        str="rock"
    elif number == 1:
        str="Spock"
    elif number == 2:
        str="paper"
    elif number == 3:
        str="lizard"
    elif number == 4:
        str="scissors"
    else:
        str="Invalid"
    return str    
    

    
def name_to_number(name):
    # fill in your code below
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return -1
    
    


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number=name_to_number(name)
    if player_number == -1:
        print "Invalid name! Valid names are rock,Spock,paper,lizard,scissors"
        return -1
    
    print "Player chooses "+name

    # compute random guess for comp_number using random.randrange()
    comp_number=random.randrange(0,5)
    print "Computer chooses "+number_to_name(comp_number)

    # compute difference of player_number and comp_number modulo five
    gfactor=(comp_number - player_number)%5

    # use if/elif/else to determine winner
    if gfactor == 1 or gfactor ==2:
        winner="Computer"
    elif gfactor == 3 or gfactor == 4:
        winner="Player"
    else:
        winner="Tie"

    # convert comp_number to name using number_to_name
    
    # print results
    if winner != "Tie":
        print winner+" wins!\n"
    else:
        print "Player and Computer tie!\n"

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


