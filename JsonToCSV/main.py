from Converter import ConvertCSV as ccsv
from pull_data import pull_data as pd
from pull_data import read_config as rc
import numpy as np
import json
from heat_map import PlotField

def main():
    config = rc()
    pull = pd(config)
#    pull.set_data()
   # print(pull.get_server_sorce())
    j = pull.get_json_data('2022pncmp_qm81') 
    pull.get_json_team_key('blue', 'frc2471')
    
    blue_one = j['alliances']['blue'][0] 

    xf = list(map(float ,blue_one['xs']))
    x = np.array(xf)
    y = np.array(list(map(float,blue_one['ys'])))

    hm = PlotField(x,y, 'test')
    hm.plot()

main()
