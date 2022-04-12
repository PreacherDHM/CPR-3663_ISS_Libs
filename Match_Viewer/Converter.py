from pull_data import pull_data as pd
import json
import csv

# converts a json file to csv
def convert(data, pull):
    with open(pull.get_output_path() + pull.get_data(), 'r') as json_file:
        json_data = json.load(json_file)

    server_data = json_data[data]
    
    csv_file = open(pull.get_output_path() +'_'+ pull.get_output_path() +'_'+ pull.get_data_frame() +'_'+ pull.get_data_section() + '.csv','w')
    
    csv_wrighter = csv.writer(csv_file)

    counter = 0

    for d in data:
        if counter == 0:
            headder = d.keys()
            csv_wrighter.writerow(headder)
            counter += 1
        csv_wrighter.writerow(d.values())

class ConvertCSV:
    def __init__(self, data):
        self.data = data
    def convert_json(self, data_frame, data_section):
        pull = pd(data_frame, data_section)
        convert(self.data,pull)
