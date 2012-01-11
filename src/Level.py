#!/usr/bin/python

import pygame
import sys

class Level:
	
	def __init__( self, block_x_dim, block_y_dim, num_x_blocks, num_y_blocks, start_block):
		
		self.block_x_dim = block_x_dim
		self.block_y_dim = block_y_dim
		self.num_x_blocks = num_x_blocks
		self.num_y_blocks = num_y_blocks
		self.start_block_x = start_block[0]
		self.start_block_y = start_block[1]



