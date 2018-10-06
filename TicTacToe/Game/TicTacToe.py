# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:47:41 2018

@author: chrtaylo
"""

import board;
import teams;

b = board.Board()
gameTeams = teams.TeamList("X","O")


def turn(board,team):
    print("Current State of Board:")
    b.printBoardStateCoordinates()
    space = int(input("Select a space for team " + team.team + ": "))
    result = b.move(team.team,space)
    if result == -1:
        #print(result)
        print("Space already taken. Please select another spot.")
        turn(board,team)
    if result != -1:
    	#print(result)
    	#b.printBoardState()
    	status = b.checkStatus(team.team)
    	if(status == 9):
    		print("Cats Game")
    		b.printBoardState()
    	elif(0 <= status <= 7):
    		print(team.team + " Wins!")
    		b.printBoardState()
    	else:
    		turn(b,team.nextTeam)


turn(b,gameTeams.firstTeam)

