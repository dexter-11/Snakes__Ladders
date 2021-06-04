#!/usr/bin/python

#
# Snake and Ladder game - Python
#

import random
import sys    

SL_MAX = 100

# snake takes you down some spaces
snakes = {
    17:7,
    54:34,
    62:19,
    98:79,
}

# ladder advances you up some spaces
ladders = {
    3:38,
    24:33,
    42:93,
    72:84,
}

def intro():
    print("\n\n##### Welcome to Snakes & Ladders Game #####")
    print("This is a text-based game, hence no GUI. Want graphics ehh?")
    print("\nAnyways here are the rules: \n")
    print("1. Both players start at position 0; the first one to get to the end of board (100) WINS! ")
    print("2. If bit by a snake, you'll go down some spaces. If you hit a ladder, VOILA! You'll advance some extra spaces. ")
    print("3. You have 3 choices while playing - 'roll', 'enter number', or 'quit' \n")
    print("   ROLL -> Roll the dice to play a random number (1-6) ")
    print("   ENTER NUMBER -> You'll play the number that you enter between 1-20 ")
    print("   QUIT -> Quit the game. The opponent WINS by default. \n")

def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Enter the name of Player 1: ").strip()     #Avoid white spaces

    player2_name = None
    while not player2_name:
        player2_name = input("Enter the name of Player 2: ").strip()

    print("\n####### Let's start. HAVE FUN :) #######\n")
    return player1_name, player2_name


def get_dice_value():
    dice_value = 0
    while True:
        dice_value = dice_value + random.randint(1, 6)
        if dice_value == 6:
            print("YAY Its a 6. Go again!")
            pass
        else:
            print("You got a " + str(dice_value))
            break
    print("You move " + str(dice_value))
    return dice_value

def got_snake_bite(old_value, current_value, player_name):
    print("\n~~~~> " + player_name + " got a SNAKE BITE. Down from " + str(old_value) + " to " + str(current_value))


def got_ladder_jump(old_value, current_value, player_name):
    print("\n$$$ " + player_name + " climbed the LADDER from " + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    
    old_value = current_value
    current_value = current_value + int(dice_value)

    if current_value > SL_MAX:
        print("Invalid move! You need " + str(SL_MAX - old_value) + " to win. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value

 def abort_win(player_name, position):
    print("\n\n" + player_name + " won the game.")
    print("####### Game Successfully Finished #######")
    sys.exit(1) 

                  
def check_win(player_name, position):
    
    if SL_MAX == position:
        print("\n\n" + player_name + " won the game.")
        print("####### Game Successfully Finished #######")
        sys.exit(1)  ####THE ONLY SYS MODULE FUNCTION


def start():
    intro()
    
    player1_name, player2_name = get_player_names()
    
    player1_current_position = 0
    player2_current_position = 0

    
    while True:
        while True:
            turn_1 = input("\n" + player1_name + ": Enter \"roll\" OR {number between 1-20} OR \"quit\" - ")
            if turn_1.isdigit():
                #temp = int(turn_1)
                if int(turn_1) not in range(1,21):
                    print("Sorry! Enter a number between 1 and 20 (inclusive).")
                    pass
                else:
                    break
            elif turn_1 in ("roll", "quit"):
                break
            else:
                print("Sorry! INVALID INPUT... Try again")
                pass
        
        if turn_1.isdigit():
            #num = int(turn_1) 
            print("You got a: " + str(turn_1))
            player1_current_position = snake_ladder(player1_name, player1_current_position, str(turn_1))
            print("Your final position is: " + str(player1_current_position))
            pass        
        else:
            if turn_1 == "roll":
                dice_value = get_dice_value()
                player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)
                print("Your final position is: " + str(player1_current_position))
                pass
            elif turn_1 == "quit":
                print(player1_name + "\n is quiting the game!")
                abort_win(player2_name, player2_current_position)      
                pass
            else:
                pass
        pass
    
        check_win(player1_name, player1_current_position)

    
    
        while True:
            turn_2 = input("\n" + player2_name + ": Enter \"roll\" OR {number between 1-20} OR \"quit\" - ")
            if turn_2.isdigit():
                #turn_2 = int(turn_2)
                if int(turn_2) in range(1,21):
                    break
                else:
                    print("Sorry! Enter a number between 1 and 20 (inclusive).")
                    continue
            elif turn_2 in ("roll", "quit"):
                break
            else:
                print("Sorry! INVALID INPUT... Try again")
                continue
        
        if turn_2.isdigit(): 
            print("You got a: " + str(turn_2))
            player2_current_position = snake_ladder(player2_name, player2_current_position, str(turn_2))
            print("Your final position is: " + str(player2_current_position))
            pass        
        else:
            if turn_2 == "roll":
                dice_value = get_dice_value()
                player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)
                print("Your final position is: " + str(player2_current_position))
                pass
            elif turn_2 == "quit":
                print(player2_name + " is quiting the game!")
                abort_win(player1_name, player1_current_position)       
                pass
            else:
                pass
        pass

        check_win(player2_name, player2_current_position)


        
if __name__ == "__main__":
    start()
