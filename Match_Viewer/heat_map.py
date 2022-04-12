import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.image as img

blue_alliances_colors = ['blue', 'royalblue', 'darkblue']
red_alliances_colors = ['red', 'maroon', 'lightcoral']

teams = []

class PlotField:
	def __init__(self,  data_name, feeled):
 
		self.feeled_path = feeled
		self.data_name = data_name
		self.red_color_solector = 0
		self.blue_color_solector = 0

		self.extent = [0, 54, 0, 27]

	def plot(self, x, y, alliances, team):
		
		plt.xlabel('x')
		plt.ylabel('y')
		
		
	   
		#plt.imshow(self.heatmap, extent=self.extent)
		#
		
		solected_color = 'white'
		if alliances == 'blue':
			teams.append('blue-'+team)
			solected_color = blue_alliances_colors[self.blue_color_solector]
			self.blue_color_solector += 1
		if alliances == 'red':
			teams.append('red-'+team)
			solected_color = red_alliances_colors[self.red_color_solector]
			self.red_color_solector += 1
			

		#plt.scatter(self.posx, self.posy)
		test_image = img.imread(self.feeled_path)
		print(test_image.shape)
		
		plt.imshow(test_image, extent=self.extent)
		plt.scatter(x % test_image.shape[1],  y % test_image.shape[0], color=solected_color, alpha=0.1, s=50)
		#plt.plot(x % test_image.shape[1], y % test_image.shape[0], color=solected_color, alpha=0.05)
		
		
		#plt.plot(self.posx,self.posy)

	def show_ps(self, prefix, suffix):
		plt.title (prefix +' '+ str(teams) + ' ' + suffix)
		plt.legend(teams, bbox_to_anchor=(1,1))
		plt.show()
	def show(self):
		plt.title (teams)
		plt.legend(teams, bbox_to_anchor=(1,1))
		plt.show()