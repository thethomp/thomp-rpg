#!/usr/bin/python

import pygame
import sys

class Map:

	def __init__( self, x_dim, y_dim ):
		self.x_dim = x_dim
		self.y_dim = y_dim
		self.active_room = None

		self.map_array = []
		for i in xrange(x_dim) :
			self.map_array.append([])
			for j in xrange(y_dim) :
				self.map_array[i].append(0)

	def getMap( self ):
		return self.map_array

	def add( self, x, y, room ):
		self.map_array[x][y] = room

	def getActiveRoom( self ):
		for i in xrange(self.x_dim):
			for j in xrange(self.y_dim):
				if self.map_array[i][j].getActive():
					return self.map_array[i][j]
		return None
