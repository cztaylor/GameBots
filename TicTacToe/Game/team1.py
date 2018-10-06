


class Team1:
	def __init__(self,team):
		self.team = team

	def makeMove(self,boardState):
		for i in range(9):
			row = (i - 1) // 3
			col = (i - 1) % 3
			if(boardState[row][col] == " "):
				return(i)



    	

