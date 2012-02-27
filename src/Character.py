#!/usr/bin/python


import pygame
from pygame.locals import *
import Block


class Character:

	def __init__( self, isPlayer, start_block, x_dim, y_dim):
		self.current_block = start_block
		self.x = x_dim
		self.y = y_dim
		self.isPlayer = isPlayer
		self.x_pos = start_block.getX() * x_dim  # x_pos and y_pos are pixel locations
		self.y_pos = start_block.getY() * y_dim
		self.leftSheet = []
		self.rightSheet = []
		self.downSheet = []
		self.upSheet = []

	# leftSheet is a list of sprite image files for left movement
	# rightSheet is a list of sprite image files for right movement
	def loadSpriteSheets( self, left, right, down, up ):
		#leftSheet = 'sprites/' + left
		#rightSheet = 'sprites/' + right
		#downSheet = 'sprites/' + down
		#upSheet = 'sprites/' + up
		leftSheetFile = open(left, 'r')
		rightSheetFile = open(right, 'r')
		downSheetFile = open(down, 'r')
		upSheetFile = open(up, 'r')
		
		for filename in leftSheetFile:
			image = pygame.image.load(filename.rstrip())
			self.leftSheet.append(image)
		for filename in rightSheetFile:
			image = pygame.image.load(filename.rstrip())
			self.rightSheet.append(image)
		for filename in downSheetFile:
			image = pygame.image.load(filename.rstrip())
			self.downSheet.append(image)
		for filename in upSheetFile:
			image = pygame.image.load(filename.rstrip())
			self.upSheet.append(image)

	def isPlayer( self ):
		return self.isPlayer

	def getCurrentBlock( self ):
		return self.current_block

	def setCurrentBlock( self, block ):
		self.current_block = block

	def getLeftSpriteSheet( self ):
		return self.leftSheet

	def getRightSpriteSheet( self ):
		return self.rightSheet

	def getDownSpriteSheet( self ):
		return self.downSheet

	def getUpSpriteSheet( self ):
		return self.upSheet

	def getXIndex( self ):
		return self.current_block.getX()

	def getYIndex( self ):
		return self.current_block.getY()

	def getX( self ):
		return self.x_pos

	def getY( self ):
		return self.y_pos

	def	getPosition( self ):
		return (self.x_pos, self.y_pos)

	# new_x and new_y are pixel locations, not map grid locations
	def setPosition( self, new_x, new_y):
		self.x_pos = new_x	
		self.y_pos = new_y	

