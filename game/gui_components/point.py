'''
Created on Jun 07, 2021

@author: sethb
'''


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
