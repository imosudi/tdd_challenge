filename = "football-league-results.txt"

def leagueResult():
	with open(filename) as result:
		#teamDetails = []
		result.next()
		for team in result:
			teamDetails = []
			team = team.split()
			try:
				team.remove('-')
				team = team[1:]
				if len(team) > 0:
					team = team
				pass 
			except Exception as e:
				pass
			if len(team)> 1:
				team = team
				for item in team:
					teamDetails.append(item)
				print teamDetails
			else:
				del team
			print teamDetails
		pass



leagueResult()