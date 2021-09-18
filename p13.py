# wamdpp to keep track on ipl team names

team_names = set()

while True:
	op = int(input(" 1 add, 2 display, 3 remove and 4 exit "))
	if op == 1:
		name = input("enter team name to be added ")
		len1 = len(team_names)
		team_names.add(name)
		len2 = len(team_names)
		if len2 > len1:
			print(name, "added")
		else:
			print(name, "already exists")
	elif op == 2:
		print(team_names)
	elif op == 3:
		name = input("enter team name to be removed")
		len1 = len(team_names)
		team_names.discard(name)
		len2 = len(team_names)
		if len2 < len1:
			print(name, "removed")
		else:
			print(name, "does not exists")
	elif op == 4:
		break
	else:
		print("invalid option ")
	
	