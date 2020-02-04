import random
all_teams = []
semi_final_teams = []
def sort_teams(tdata):
	return tdata[1]
def num_of_teams(n):
	matches = []
	count_teams = []
	for x in range(0,len(n)):
		team1 = n[x]
		for y in range(x+1,len(n)):
			team2 = n[y]
			matches.append((team1,team2))
	double = matches*2
	#print(double)
	for points in double:
		ran = random.randint(1,2) 
		rand_points = f"{points} : {points[ran-1]}"
		#print(rand_points)
		wteams = f"{points[ran-1]}"
		count_teams.append(wteams)
	sub = "CSK"
	sub1 = "PUN"
	sub2 = "MI"
	sub3 = "RCB"
	sub4 = "DC"
	sub5 = "RR"
	sub6 = "SRH"
	sub7 = "KKR"
	count1 = 0
	count2 = 0
	count3 = 0
	count4 = 0
	count5 = 0
	count6 = 0
	count7 = 0
	count8 = 0
	#print(count_teams)
	for i in count_teams:
		if sub in i:
			count1 = count1+1
		elif sub1 in i:
			count2 = count2+1
		elif sub2 in i:
			count3 = count3+1
		elif sub3 in i:
			count4 = count4+1
		elif sub4 in i:
			count5 = count5+1
		elif sub5 in i:
			count6 = count6+1
		elif sub6 in i:
			count7 = count7+1
		elif sub7 in i:
			count8 = count8+1
	all_teams.append(("CSK",count1*2))
	all_teams.append(("PUN",count2*2))
	all_teams.append(("MI",count3*2))
	all_teams.append(("RCB",count4*2))
	all_teams.append(("DC",count5*2))
	all_teams.append(("RR",count6*2))
	all_teams.append(("SRH",count7*2))
	all_teams.append(("KKR",count8*2))
	return all_teams
def play_offs(a):
	print(f"LEAGUE_MATCHES_WITH_POINTS:{a}")
	print("")
	
	for semis in a[4:]:
		semi_final_teams.append(semis[0])
	playoffs = semi_final_teams
	print(f"PLAYOFF_TEAMS:{playoffs}")
	print("")
	
	top_two = tuple(playoffs[2:])
	a = random.randint(1,2)
	final_list = []
	final_team1 = f"{top_two[a-1]}"
	final_list.append(f"{final_team1}")
	print(f"playoff1:{top_two}")
	print(f"playoff1_winner:{final_team1}")
	print("")
	playoffs3 = []
	if final_team1 in top_two[0]:
		playoffs3.append(top_two[1])
	else:
		playoffs3.append(top_two[0])
	#print(playoffs3)
	
	last_two = tuple(playoffs[0:2])
	b = random.randint(1,2)
	last_team2 = f"{last_two[b-1]}"
	print(f"playoff2:{last_two}")
	print(f"playoff2_winner:{last_team2}")
	print("")
	playoffs3.append(f"{last_team2}")
	print(f"playoff3:{playoffs3}")
	
	eliminator = tuple(playoffs3[0:])
	c = random.randint(1,2)
	final_team2 = f"{eliminator[c-1]}"
	print(f"playoff3_winner:{final_team2}")
	print("")
	final_list.append(f"{final_team2}")
	print(f"final_teams:{final_list}") 
	
	final_match = ((final_team1,final_team2))
	#print(final_match)
	team = random.randint(1,2)
	ipl_winner = f"{final_match[team-1]}"
	print(f"IPL WINNER:{ipl_winner}")
	
	
def main():
	teams = ["PUN","MI","RCB",'DC',"RR","SRH","KKR","CSK"]
	num_of_teams(teams)
	a = sorted(all_teams,key=sort_teams)
	play_offs(a)
	
if(__name__=="__main__"):
	main()