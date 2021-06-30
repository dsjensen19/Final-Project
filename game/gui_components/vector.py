'''
Created on Jun 07, 2021

@author: sethb
'''
from math import(
	cos, sin, atan, 
	radians as toRadians, 
	degrees as toDegrees
)

class Vector():
	def __init__(self, dx, dy):
		self.dx = dx
		self.dy = dy

		#ToDo: Finish the __init Statement

	@property
	def angle(self):
		if self.dx == 0.0:
			if self.dy < 0.0:
				return 270
			else:
				return 90
		else:
			if self.dx < 0:
				return toDegrees(atan(self.dy/self.dx))+180
			return toDegrees(atan(self.dy/self.dx))

	@angle.setter
	def angle(self, value):
		if self.magnitude == 0:
			self.magnitude = 1
		magnitude = self.magnitude
		self.dx = magnitude * cos(toRadians(value))
		self.dy = magnitude * sin(toRadians(value))

	@property
	def magnitude(self):
		return (self.dx**2 + self.dy**2)**(1/2)

	@magnitude.setter
	def magnitude(self, value):
		angle = self.angle
		self.dx = value * cos(toRadians(angle))
		self.dy = value * sin(toRadians(angle))

	def copy(self):
		return Vector(self.dx,self.dy)
