# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:47:41 2018

@author: chrtaylo
"""

import board;



b = board.Board()





b.move("X",1)
b.move("X",5)
b.move("X",9)
b.move("O",6)
b.move("O",3)

b.printBoardStateCoordinates()

status = b.checkStatus("X")

print(status)
