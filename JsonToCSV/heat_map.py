import numpy as np 
import matplotlib.pyplot as plt

class PlotField:
    def __init__(self, x, y, data_name):
        self.posx = x
        self.posy = y
        self.data_name = data_name

    def plot(self):
        plt.title = self.data_name
        plt.xlabel = 'x'
        plt.ylabel = 'y'
       
        plt.plot(self.posx,self.posx)
        plt.show()
