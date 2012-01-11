#!/usr/bin/python

import pygame
import Block
import Character

# transition block, inherits all methods and attributes from Block.py
class TransitionBlock( Block ):
	
	destinationRoom = None
	destinationBlock = None

	def	setDestinationBlock( room, block ):
		self.destinationRoom = room
		self.destinationBlock = block	
	


