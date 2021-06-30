'''
Created on Jun 07, 2021

@author: sethb
'''

from abc import ABC

from game.gui_components.point import Point
from game.gui_components.sprite import Sprite
from game.gui_components.vector import Vector

class Game_Object(ABC):
	def __init__(self, **kwargs):
		self.center = Point(0, 0)
		self.velocity = Vector(0, 0)
		self.sprite = Sprite()
		self._dRotation = 0.0
		self.is_in_animation = False

		if "center" in kwargs.keys():
			self.center = kwargs["center"]
		else:
			if "x" in kwargs.keys():
				self.x = kwargs["x"]
			if "y" in kwargs.keys():
				self.y = kwargs["y"]
			 
		if "velocity" in kwargs.keys():
			self.velocity = kwargs["velocity"]
		else:
			if "dx" in kwargs.keys():
				self.dx = kwargs["dx"]
			if "dy" in kwargs.keys():
				self.dy = kwargs["dy"]

		if "rotation" in kwargs.keys():
			self.rotation = kwargs["rotation"]

		if "dRotation" in kwargs.keys():
			self._dRotation = kwargs["dRotation"]

		if "image" in kwargs.keys():
			self.image = kwargs["image"] 

	def draw(self):
		self.sprite.draw(self.x, self.y)

	def update(self):
		self.center.move(self.velocity)
		self.rotation += self._dRotation

		# if self.animation:
		# 	if self.animation.is_finished: 
		# 		self.animation = None
		# 		self.is_in_animation = False
		# 	else:
		# 		self.animation.update()
		

	@property
	def x(self):
		return self.center.x
	@x.setter
	def x(self, value):
		self.center.x = value
		
	@property
	def y(self):
		return self.center.y
	@y.setter
	def y(self, value):
		self.center.y = value

	@property
	def dx(self):
		return self.velocity.dx
	@dx.setter
	def dx(self, value):
		self.velocity.dx = value
		
	@property
	def dy(self):
		return self.velocity.dy
	@dy.setter
	def dy(self, value):
		self.velocity.dy = value

	@property
	def rotation(self):
		return self.sprite.rotation
	@rotation.setter
	def rotation(self, value):
		self.sprite.rotation = value

	@property
	def dRotation(self):
		return self._dRotation
	@dRotation.setter
	def dRotation(self, value):
		self._dRotation = value

	@property
	def image(self):
		return self.sprite.image
	@image.setter
	def image(self, value):
		self.sprite.image = value
