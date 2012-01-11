#!/usr/bin/python

import pygame
from pygame.locals import *
import Character

class NPC( Character ):

	self.state = 0

	def update( self ):
		if self.state == 0:
			#update position
			self.state = 1
		elif self.state == 1:
			#update position:
	
	def render( self ):		
		return
