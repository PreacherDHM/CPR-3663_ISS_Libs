from Converter import ConvertCSV as ccsv
from pull_data import pull_data as pd
from pull_data import read_config as rc
from heat_map import PlotField
import numpy as np
import json

import sys


def main():
	config = rc()
	pull = pd(config)
	#pull.set_data()
	#print(pull.get_server_sorce())
	j = pull.get_json_data('2022pncmp_qm81') 
	pull.get_json_team_key('red', 'frc3663')
	
	j_data = pull.get_json_data('frc3663')

	data = j_data['alliances']['red']
	blue_one = j['alliances']['red'][1] 


	
	x = np.array(list(map(float ,data['xs'])))
	y = np.array(list(map(float,data['ys'])))

	hm = PlotField(data['team_key'] + 'all maches, ', 'Feeled.png')
	#hm.plot()

	args = sys.argv[1:]
	arg_len = len(args)
	arg_pos = 0


	teams = [] # red/frc3663 blue/frc2910
	json_data = None
	
	print('arg len: ' + str(arg_len))
	while True:
		if args[arg_pos] == '-t': # get all match data for team
			
			teams = args[arg_pos +1].split(' ')
			print(teams)
			
			for team in teams:
				a = team.split('/')[0]
				t = team.split('/')[1]
				json_data = pull.get_json_team_key(a, t)
				data = json_data['alliances'][a]
				x = np.array(list(map(float ,data['xs'])))
				y = np.array(list(map(float,data['ys'])))
				print('reading')
				hm.plot(x,y, a, t)
			hm.show_ps('all maches', 'comp')
			return
		if args[arg_pos] == '-mt': # get team in match
			arg_pos +=1 
			teams.append(args[arg_pos])
			
			continue
		if args[arg_pos] == '-m': # get teams in a match
			arg_pos += 1
			teams.append(args[arg_pos])
			continue
		if args[arg_pos] == '-u': # updata data
			pull.set_data()
			continue
		

		if args[arg_pos] == '':
			return
		
		if arg_len == arg_pos:
			return
		arg_pos +=1

main()
