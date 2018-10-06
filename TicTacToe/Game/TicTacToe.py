# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:47:41 2018

@author: chrtaylo
"""

import board;
import teams;
import team1;
#import team2;

t1 = team1.Team1("X")

b = board.Board()
gameTeams = teams.TeamList("X","O")


def turn(board,team):
    print("Current State of Board:")
    b.printBoardStateCoordinates()
    if(team.team == "X"):
    	result = b.move(team.team,t1.makeMove(b.state))
    	#need to count invalid moves. if too many, team loses.
    else:
	    space = int(input("Select a space for team " + team.team + ": "))
	    result = b.move(team.team,space)

    if result == -1:
        print("Space already taken. Please select another spot.")
        turn(board,team)
    else:
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

