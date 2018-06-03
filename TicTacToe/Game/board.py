# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:20:40 2018

@author: chrtaylo
"""

class Board:
    def __init__(self):
        self.coordinates = [["1","2","3"],["4","5","6"],["7","8","9"]]
        self.state = [[" "," "," "],[" "," "," "],[" "," "," "]]
        
    def StateCoordinate(self,row,col,SCType):
        if SCType == "State":
            return(self.state[row][col])
        elif SCType == "Coordinates":
            return(self.coordinates[row][col])
        elif SCType == "StateWithCoordinates":
            if self.state[row][col] == " ":
                return(self.coordinates[row][col])
            else:
                return(self.state[row][col])
        else:
            return "Invalid SCType"
        
    def printBoard(self,PrintType):
        print()
        print(" " + self.StateCoordinate(0,0,PrintType) + " | " + self.StateCoordinate(0,1,PrintType) + " | " + self.StateCoordinate(0,2,PrintType) + " ")
        print("-----------")
        print(" " + self.StateCoordinate(1,0,PrintType) + " | " + self.StateCoordinate(1,1,PrintType) + " | " + self.StateCoordinate(1,2,PrintType) + " ")
        print("-----------")
        print(" " + self.StateCoordinate(2,0,PrintType) + " | " + self.StateCoordinate(2,1,PrintType) + " | " + self.StateCoordinate(2,2,PrintType) + " ")
    
    def printBoardState(self):
        self.printBoard("State")
    
    def printBoardCoordinates(self):
        self.printBoard("Coordinates")
        
    def printBoardStateCoordinates(self):
        self.printBoard("StateWithCoordinates")
        
    def move(self,team,coordinate):
        row = (coordinate - 1) // 3
        col = (coordinate - 1) % 3
        if self.state[row][col] == " ":
            self.state[row][col] = team
            return(coordinate)
        else:
            return(-1)
    
    def checkStatus(self,team):
        for n in range(3):
            if all(x == team for x in self.state[n][:]):
                return(n)
            elif all(x == team for x in [x[n] for x in self.state]):
                return(n + 3)
        if self.state[1][1] == team:
            if self.state[0][0] == team and self.state[2][2] == team:
                return(6)
            if self.state[2][0] == team and self.state[0][2] == team:
                return(7)
        return(-1)
                





