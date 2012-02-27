#!/usr/bin/python

import pygame
import sys
import Block
from pygame.locals import *

class Room:

	def __init__( self, map_x_coord, map_y_coord, x_dim, y_dim, x_block_dim, y_block_dim, path, name ) :
		self.x_dim = x_dim
		self.y_dim = y_dim
		self.x_block_dim = x_block_dim
		self.y_block_dim = y_block_dim
		self.max_x_index = x_dim/x_block_dim 
		self.max_y_index = y_dim/y_block_dim 
		self.map_x_coord = map_x_coord
		self.map_y_coord = map_y_coord
		self.path = path
		self.name = name
		self.csv_path = path + '/' + name + '/' + name + '.csv'
		self.image_path = path + '/' + name + '/' + name + '.jpg'	
		self.image = pygame.image.load(self.image_path).convert()
		self.is_active = False

		self.npcs = []
	
		print 'max_x_index:' + str(self.max_x_index)
		print 'max_y_index:' + str(self.max_y_index)
	
		# create room array
		self.room = []  # array of block objects
		for i in xrange(self.max_x_index):
#			print 'room i:' + str(i)
			self.room.append([])
			for j in xrange(self.max_y_index):
#				print 'room i,j:' + str((i,j)) 
				self.room[i].append(Block.Block(i,j))

		self.syncCSV( self.csv_path )

	def reloadRoomImage( self ):
		self.image = pygame.image.load(self.image_path).convert()
		return self	

	def getMaxX( self ):
		return self.max_x_index

	def getMaxY( self ):
		return self.max_y_index

	def getScreenCoords( self ):
		return (self.x_dim, self.y_dim)

	def getRoom( self ):
		return self.room

	def getImage( self ):
		return self.image

	def makeActive( self, active ):
		self.is_active = active

	def getActive( self ):
		return self.is_active

	def getCharBlock( self ):
		for i in xrange(self.max_x_index):
			for j in xrange(self.max_y_index):
				if self.room[i][j].containsChar():
					return self.room[i][j]
		return None

	# private method for setting initial state of blocks
	def syncCSV( self, filepath ):
		# build 2d array from csv data
		csv = open(filepath, 'r')
		csv_array = []
		i = 0
		for line in csv:
			temp = line.replace('\n','')
			csv_array.append([])
			for subline in temp.split(';'):
				csv_array[i].append(subline)
			i += 1
	
		print csv_array

		#sync 2d csv array with block array
		for i in xrange(self.max_x_index):
			for j in xrange(self.max_y_index):
				if csv_array[j][i].find('x') != -1:
					self.room[i][j].setWall(True)
				if csv_array[j][i].find('i') != -1:
					self.room[i][j].setInteractable(True)
					self.room[i][j].setMessage( csv_array[j][i].split(':')[1] )
				if csv_array[j][i].find('start') != -1:
					self.room[i][j].setChar(True)
		
				
	def addTransition( self, source_x, source_y, room, dest_x, dest_y ):
		self.room[source_x][source_y].addBlockTransition( room, dest_x, dest_y )
		
	def addNPC( self, npc ):
		self.npcs.append(npc)
	
