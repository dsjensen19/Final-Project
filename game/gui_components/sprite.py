'''
Created on Jun 07, 2021

@author: sethb
'''

import arcade
import constants
from arcade import(
	draw_texture_rectangle,
	load_texture
)

class Sprite():

	"""Sets initall values using kwargs
	kwargs
	type,	name,		default value,	description
	float, 	rotation, 	0.0,			theta off of 0 degrees default
	int,	alpha,		255,			alpha value of sprite when printed	
	string,	image_name, "none",			just the name of the image file 
		Image is constants.file_path + "image_name" + .png
	"""
	def __init__(self, **kwargs):
		self._image = None
		self._texture = None
		self._width = None
		self._height = None
		self._rotation = 0.0
		self._alpha = 255


		if "rotation" in kwargs.keys():
			self.rotation = kwargs["rotation"]

		if "alpha" in kwargs.keys():
			self._alpha = kwargs["alpha"] 

		if "image_path" in kwargs.keys():
			self.image = kwargs["image_name"]
		else:
			self.image = "none"


	@property
	def rotation(self):
		return self._rotation
	@rotation.setter
	def rotation(self, value):
		self._rotation = value

	@property
	def image(self):
		return self._image
	@image.setter
	def image(self, image_file_path):
		self._image = constants.IMAGE_DIRECTORY + image_file_path + ".png"
		self._texture = load_texture(self.image)
		self._width = self._texture.width
		self._height = self._texture.height


	def draw(self, x, y):
		alpha = 255
		# arcade.draw_text(f"{x:.2f}, {y:.2f}",x,y,arcade.color.BLACK)
		draw_texture_rectangle(x, y, self._width, self._height, self._texture, self.rotation, alpha)

		
