#!/usr/bin/python

import pygame
import sys
import Character
import Room

class Block:
	
	def __init__( self, x_coord, y_coord ):
		
		self.isWall = False
		self.isInteractable = False 
		self.contains_char = False
		self.x = x_coord
		self.y = y_coord
		self.leftBlock = None
		self.rightBlock = None
		self.upBlock = None
		self.downBlock = None
		self.hasTransition = False
		self.dest_x = None
		self.dest_y = None
		self.dest_room = None
		self.message = ""


	def isWall( self ):
		return self.isWall

	def setWall( self, wall_bool ):
		self.isWall = wall_bool

	def containsChar( self ):
		return self.contains_char

	def setChar( self, present, player=None ):
		self.contains_char = present
		if present == True and player == None:
			return
		elif present == True:
			player.setCurrentBlock(self)

	def getX( self ):
		return self.x

	def getY( self ):
		return self.y

	def addTransition( self, room, dest_x, dest_y ):
		self.hasTransition = True
		self.dest_x = dest_x
		self.dest_y = dest_y
		self.dest_room = room

	def getDestinationRoom( self ) :
		return self.dest_room

	def getDestinationX( self ):
		return self.dest_x

	def getDestinationY( self ):
		return self.dest_y

	def setInteractable(self, boolean):
		self.isInteractable = boolean

	def isInteractable( self ):
		return self.isInteractable

	def setMessage( self, msg ):
		self.message = msg

	def getMessage( self ):
		return self.message	

