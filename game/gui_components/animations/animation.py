from abc import ABC
from abc import abstractmethod

import constants

"""
The animation class is a parent class that takes in a game object and a time.
1: The init stores the objects Velocity, and rotation position values
2: The set_inital_values function sets those values to initiial values to simulat an animation (Defined by child class)
3: The Update function changes those values if needed for exampple to accelorat an object durin the animation.
	(can be defined by the child class as long as the super is called)
4: the set final values functionn is used to set the values to zero or its initial values that were sotred in init (Defined by child class)

Atributes 
	is_finished
	_time_end
	_time
	_game_object
	_initial_position
	_initial_velocity
	_initial_rotation
functions
	__init__(game_object, time)
	set_initial_values
	update
	set_final_values

"""
class Animation(ABC):
	def __init__(self, game_object, time = 1):
		self.is_finished = True
		if game_object.is_in_animation:
			return
		else:
			self.is_finished = False
			game_object.is_in_animation = True
			self._time_end = time / constants.REFRESH_RATE
			self._time = 0
			
			self._game_object = game_object
			self._initial_position = self._game_object.center.copy()
			self._initial_velocity = self._game_object.velocity.copy()
			self._initial_rotation = self._game_object.rotation

			self.set_initial_values()

	def update(self):
		self._time += 1

		if self._time >= self._time_end:	
			self.set_final_values()
		# if self._time > self._time_end+100:
			self.is_finished = True
			self._game_object.is_in_animation = False
	@abstractmethod
	def set_initial_values(self):
		pass
	@abstractmethod
	def set_final_values(self):
		pass
