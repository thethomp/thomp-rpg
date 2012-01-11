#!/usr/bin/python

import pygame
from pygame.locals import *
import os
from sys import exit
from gameobjects.vector2 import Vector2
import math
import Character
import MapLoader

pygame.init()

# Constant values
BLOCK_SIZE_X = 64.
BLOCK_SIZE_Y = 64.
clock = pygame.time.Clock()
fps = 10
speed = 25
start = pygame.time.get_ticks()
delay = 1000/fps
last_update = 0 
sprite_speed = 5

# Map object setup
loader = MapLoader.MapLoader('/home/thomp/pygame/thomp-rpg/build2/')
level_1_map = loader.loadLevel1()
screen = pygame.display.set_mode(level_1_map.getActiveRoom().getScreenCoords(), 0, 32)


#ml1 = MapLoader.MapLoader(BLOCK_SIZE_X,BLOCK_SIZE_Y,640,640,'/home/thomp/pygame/thomp-rpg/build1/maps/level1/room1/room1-64.jpg', True)
#ml2 = MapLoader.MapLoader(BLOCK_SIZE_X,BLOCK_SIZE_Y,640,640,'/home/thomp/pygame/thomp-rpg/build1/maps/level1/room2/room2-64.jpg', False)
#current_map = ml1
#screen = pygame.display.set_mode((current_map.x, current_map.y), 0, 32)
#background = current_map.getImage()
#current_map.parseCSV('maps/level1/room1/room1.csv')
#current_map.setUpLink(ml2)
#ml2.parseCSV('maps/level1/room2/room2.csv')
#ml2.setDownLink(ml1)


# Character object setup
start_block = level_1_map.getActiveRoom().getCharBlock()


start_pos = Vector2(64,64)
player = Character.Character(True,start_pos) 
player.loadSpriteSheets('sprites/playerLeft.txt', 'sprites/playerRight.txt')
leftSpriteSheet = player.getLeftSpriteSheet()
rightSpriteSheet = player.getRightSpriteSheet()
frame = 0 
image = rightSpriteSheet[frame]  # starting character sprite frame
sprite_pos = player.getPosition()


#def move( x_distance, y_distance, current_pos, restricted, upEE, downEE, sprite_sheet ) :
def move( x_distance, y_distance, current_pos, ml, sprite_sheet ) :
	global image
	global frame
	global current_map
	# Check to see if block is restricted
	next_pos_x = (current_pos[0] + x_distance)/BLOCK_SIZE_X + 1
	next_pos_y = (current_pos[1] + y_distance)/BLOCK_SIZE_Y + 1
	print 'next_pos:' + str([next_pos_x, next_pos_y])
	print 'player_pos: ' + str(player.getPosition())
	if [next_pos_x, next_pos_y] in restricted :
		print 'in restricted'
		screen.blit(ml.getImage(), (0,0))
		pygame.time.delay(50)
		frame = 0
		image = sprite_sheet[frame]
		screen.blit(image,player.getP 	osition())
		pygame.display.update()
		return
	elif ml.getUpLink() != None and [next_pos_x, next_pos_y] in upEE :
		print 'in up entrance'
		current_map = ml.getUpLink()
		player.setPosition(current_map.getUpEEVec())
		screen.blit(ml.getImage(),(0,0))
		pygame.time.delay(50)
		frame = 0
		image = sprite_sheet[frame]
		screen.blit(image,player.getPosition())
		pygame.display.update()
		return
	elif ml.getDownLink() != None and [next_pos_x, next_pos_y] in downEE :
		print 'in down entrance'
		current_map = ml.getDownLink()
		player.setPosition(current_map.getDownEEVec())
		screen.blit(ml.getImage(), (0,0))
		pygame.time.delay(50)
		frame = 0
		image = sprite_sheet[frame]
		screen.blit(image,player.getPosition())
		pygame.display.update()
		return
	sprite_pos = player.getPosition()
	for spriteframe in sprite_sheet:
		print 'in default'
		sprite_pos.x += x_distance/len(sprite_sheet)
		sprite_pos.y += y_distance/len(sprite_sheet)
		player.setPosition(sprite_pos)
		screen.blit(current_map.getImage(), (0,0))
		pygame.time.delay(50)
		image = sprite_sheet[frame]
		screen.blit(image,player.getPosition())
		pygame.display.update()
		frame +=1
		if frame >= len(sprite_sheet):
			frame = 0

while True:

	t = pygame.time.get_ticks()

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	pressed_keys = pygame.key.get_pressed()

	current_map = level_1_map.getCurrentRoom()

	# Left Arrow or A movement
	if pressed_keys[K_LEFT] or pressed_keys[K_a]:
		move( -1, 0, player.getPosition(), current_map, leftSpriteSheet )
	## Right Arrow or D movement
	elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
		move( 1, 0, player.getPosition(), current_map, rightSpriteSheet )
	# Up Arrow or W movement
	if pressed_keys[K_UP] or pressed_keys[K_w]:
		move( 0, -1, player.getPosition(), current_map, leftSpriteSheet )
	# Down Arrow or S movement
	elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
		move( 0, 1, player.getPosition(), current_map, leftSpriteSheet )

	frame = 1
	screen.blit(current_map.getImage(), (0,0))
	screen.blit(image, player.getPosition()) 
	
	pygame.display.update()
