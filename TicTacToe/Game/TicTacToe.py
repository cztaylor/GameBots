# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:47:41 2018

@author: chrtaylo
"""

import board;

b = board.Board()

b.move("X",1)

def turn(board,team):
    space = int(input("Select a space for team " + team + ": "))
    result = b.move(team,space)
    if result == -1:
        print("Space already taken. Please select another spot.")
        turn(board,team)
    print(result)
    b.printBoardState()

turn(b,"X")

#b.move("X",1)
#b.move("X",5)
#b.move("X",9)
#b.move("O",6)
#b.move("O",3)
#
#b.printBoardStateCoordinates()
#
#status = b.checkStatus("X")
#
#print(status)
