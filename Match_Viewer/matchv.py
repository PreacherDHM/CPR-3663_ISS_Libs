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

	hm = PlotField('all maches, ', 'Feeled.png')
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
			match = args[arg_pos]
			arg_pos +=1
			target_team = args[arg_pos].split(' ')
			for team in target_team:
				x = []
				y = []
				t = team.split('/')[1]
				a = team.split('/')[0]

				json_data = pull.get_json_data(match)['alliances'][a]
				print(a)
				for team in range(3):
					print(team)
					if json_data[team]['team_key'] == t:
						for xs in json_data[team]['xs']:
							if xs != None and xs != 'null':
								x.append(float(xs))
						for ys in json_data[team]['ys']:
							if ys != None and ys != 'null':
								y.append(float(ys))
						
						ny = np.array(y)
						nx = np.array(x)
						hm.plot(nx,ny,a, json_data[team]['team_key'])
						
							
			hm.show()
			
			break
		if args[arg_pos] == '-m': # get teams in a match
			
			arg_pos +=1 
			match = args[arg_pos]
			json_data = pull.get_json_data(match)['alliances']
			for alliances in json_data:
				x = []
				y = []
				print(alliances)
				for team in range(3):
					print(team)
					for xs in json_data[alliances][team]['xs']:
						if xs != None and xs != 'null':
							x.append(float(xs))
					for ys in json_data[alliances][team]['ys']:
						if ys != None and ys != 'null':
							y.append(float(ys))
					ny = np.array(y)
					nx = np.array(x)
					hm.plot(nx,ny,alliances, json_data[alliances][team]['team_key'])
							
			hm.show()
			break
		if args[arg_pos] == '-u': # updata data
			pull.set_data()
			break
		

		if args[arg_pos] == '':
			return
		
		if arg_len == arg_pos:
			return
		arg_pos +=1

main()
