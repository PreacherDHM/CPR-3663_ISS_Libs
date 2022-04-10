import requests 
from time import sleep
from threading import Thread
import json
import io
import os

from error_codes import error as er 

class read_config:
    config_path = './ISS.config'
    data_server = '' 
    data_server_options = '' 
    data_project_name = '' 
    data_output_path = '' 
    data_url = [] 
    data_server_section = '' 
    data_number_of_frames = 0
    data_frame_options = ''
    data_server_frames = [] 

    def get_config(self):

        if False == os.path.exists(self.config_path):
            print(er.no_config_file)
            return

        config_file = open(self.config_path, 'r') 
        
        while True: 

            
            line = ''+config_file.readline()
            if line == '':
                break

            # replacing certen characters
            line = line.replace(" ","")
            line = line.replace("\n","")

            # splitting the data
            print('line: ' + line)
            name = line.split('~')[0]
            data = line.split('~')[1]

            print('name ' + name + '\n' + 'data ' + data)
            
            if name == 'server-options':
                self.data_server_options = data 
                continue
            if name == 'project-name':
                self.data_project_name = data
                continue
            if name == "output-path":
                self.data_output_path = data
                continue
            if name == 'server-name':
                self.data_server = data
                print('server_data: ' + self.data_server)
                continue
            if name == 'server-section':
                self.data_server_section = data
            if name == 'server-frame-option':
                self.data_frame_options = data
            if name == 'server-nomber-of-frames':
                self.data_number_of_frames = int(data)
            if name == 'set':
                if len(data.split(':')) >= 1:
                    data = data.replace(":","")
                    for x in range(self.data_number_of_frames):
                        self.data_server_frames.append(data +  str(x) + self.data_frame_options)

                self.data_server_frames.append(data)
                    
                
            print('found none')
        print('End of File --------------')
        
        for frame in list(self.data_server_frames):
            self.data_url.append(self.data_server + '/' + self.data_server_section + '/' + frame  + '?' + self.data_server_options)

class pull_data:
    def __init__(self, config):
        self.config = config 
        self.threads = []
        self.config.get_config()

    def get_project_name(self):
        return self.config.data_project_name

    def get_data_frame(self):
        return self.config.data_server_frames

    def get_data_section(self):
        return self.config.data_server_section

    def get_server_sorce(self):
        return self.config.data_url

    def get_server(self):
        return self.config.data_server

    def get_output_path(self):
        return self.config.data_output_path

    def set_data_threaded(self):
        for i in range(len(self.config.data_url)): 
            t = Thread(target=self.task, args=(i,))
            self.threads.append(t)
            t.start()


    def set_data(self):
        for i in range(len(self.config.data_url)):
            self.task(i)
            
    def task(self, i):
        print(self.config.data_server_frames[i])
        print(i)
        print('---------------------------------')
        print(self.config.data_url[i])
        while True:
            try:
                r = requests.get(self.config.data_url[i])
                content = r.content

                print('Found data at URL: ' + self.config.data_url[i]) 
                print('data gathering sucsesfol!!!')
                json_file = open(self.config.data_output_path + self.config.data_project_name +'-'+ self.config.data_server_frames[i].split('/')[0] + '.json', 'wb')
                json_file.write(content)
                json_file.close()
                return
            except:
                print(er.cant_connect + ' Server: ' + self.config.data_url[i])
                return

    def get_json_data(self, data):
                json_file = open(self.config.data_output_path + self.config.data_project_name +'-'+ data + '.json', 'r')
                json_load = json.load(json_file)
                json_file.close()
                return json_load
