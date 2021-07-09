'''
Created on Jun 07, 2021

@author: sethb
'''


from math import sqrt


class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

		#ToDo: Finish the __init Statement


	def move(self, velocity):
		self.x += velocity.dx
		self.y += velocity.dy

	def copy(self):
		return Point(self.x,self.y)

	def distance(self, point):
		distance = sqrt((point.x - self.x)**2 + (point.y - self.y)**2)
		return distance