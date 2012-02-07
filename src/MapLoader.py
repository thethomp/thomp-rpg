#!/usr/bin/python

import pygame
from pygame.locals import *
import string
import Map
import Room

class MapLoader :

	def __init__( self, path ) :
		self.path = path


	def loadLevel1( self ) :
		level_path = '/level1/'
		level1 = Map.Map(1,2)
		# room 1 setup
		room1 = Room.Room(0,0,1280,960,64,64, self.path + level_path, 'room1')
		room1.makeActive(True)
		# room 2 setup
		#room2 = Room.Room(0,1,640,640,64,64, self.path + level_path, 'room2')
		room2 = Room.Room(0,1,1280,960,64,64, self.path + level_path, 'room2')
		# add entrance/exit transitions
		room1.addTransition(10,0, room2, 9,14 )
		room2.addTransition(9,14, room1, 10,0 )
		# add rooms to level
		level1.add(0,0,room1)
		level1.add(0,1,room2)
		return level1

