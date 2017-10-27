import sys
import random

tictactoe = {
             1:' ', 2:' ', 3:' ',
             4:' ', 5:' ', 6:' ',
             7:' ', 8:' ', 9:' '
            }   # the tic-tac-toe board

def draw_board():
    print ("   |   |   ")
    print (" "+tictactoe[1]+" | "+tictactoe[2]+" | "+tictactoe[3]+" ")
    print ("___|___|___")
    print ("   |   |   ")
    print (" "+tictactoe[4]+" | "+tictactoe[5]+" | "+tictactoe[6]+" ")
    print ("___|___|___")
    print ("   |   |   ")
    print (" "+tictactoe[7]+" | "+tictactoe[8]+" | "+tictactoe[9]+" ")
    print ("   |   |   ")
    
def win_is_true(ch) :
    win_states = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]
    for x in win_states :
        if (tictactoe[x[0]] == ch and tictactoe[x[1]] == ch and tictactoe[x[2]] == ch) :
            return True
    return False
    
print ("Welcome to Tic Tac Toe... All the best!!")
p1 = input ("Enter name of player 1 : ")
p2 = input ("Enter name of player 2 : ")
chance = random.randint(1,2)
if chance == 1 :
    print ("Player 1 gets the first move!!")
else :
    print ("Player 2 gets the first move!!")    
moves = 0
print ("The board positions are as follows : ")
print ("   |   |   ")
print (" 1 | 2 | 3 ")
print ("___|___|___")
print ("   |   |   ")
print (" 4 | 5 | 6 ")
print ("___|___|___")
print ("   |   |   ")
print (" 7 | 8 | 9 ")
print ("   |   |   ")
marked_areas = []
while moves < 9 :
    print ("The board currently looks like : ")
    draw_board()
    place = int (input ("Please enter the place where you want to make a move player " + str(chance) + " : "))
    if (place <= 0 or place > 9) :
        print ("Invalid move! Please choose a valid position...")
    elif (place in marked_areas) :
        print ("That move has already been made fool!!")
    else :
        marked_areas.append (place)
        chx = ' '
        if chance == 1 :
            tictactoe[place] = 'O'
            chance = 2
            chx = 'O'
        else :
            tictactoe[place] = 'X'
            chance = 1
            chx = 'X'
        if win_is_true(chx) :
            print ("Wohoo!! Congo!!")
            if chance == 2 :
                print (p1 + " is the winner!")
            else :
                print (p2 + " is the winner!")
            print ("The board currently looks like : ")
            draw_board()    
            sys.exit()
    moves += 1
print ("Its a draw man!!")
print ("The board currently looks like : ")
draw_board()
print ("Bye Bye! Do come back...")
    
