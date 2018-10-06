


class TeamNode:
    def __init__(self,team):
        self.team = team
        self.nextTeam = None

class TeamList:
	def __init__(self,team1,team2):
		self.firstTeam = TeamNode(team1)
		self.secondTeam = TeamNode(team2)
		self.firstTeam.nextTeam = self.secondTeam
		self.secondTeam.nextTeam = self.firstTeam
