#!/usr/bin/python

import pygame
from pygame.locals import *
from sys import exit
import Character
import MapLoader
import Map
import Block
import Room
import math


pygame.init()

# Constants
BLOCK_SIZE_X = 64
BLOCK_SIZE_Y = 64

# Map object setup
loader = MapLoader.MapLoader('/home/thomp/python/thomp-rpg/src/maps')
screen = pygame.display.set_mode((1280,960), pygame.RESIZABLE, 32)
level_1_map = loader.loadLevel1()

# Character object setup
start_block = level_1_map.getActiveRoom().getCharBlock()
player = Character.Character(True, start_block, 64, 64)
player.loadSpriteSheets('playerDown.txt', 'playerDown.txt', 'playerDown.txt', 'playerUp.txt')
leftSpriteSheet = player.getLeftSpriteSheet()
rightSpriteSheet = player.getRightSpriteSheet()
downSpriteSheet = player.getDownSpriteSheet()
upSpriteSheet = player.getUpSpriteSheet()
frame_index = 0
image = rightSpriteSheet[frame_index]

# NPC object setup
#npc = Character.Character(False, level_1_map.getActiveRoom().getRoom()[3][3], 64, 64)
#npc.setPosition(4*64, 4*64)
#npc.loadSpriteSheets('npc1Left.txt', 'npc1Right.txt', 'npc1Down.txt', 'npc1Up.txt')
#npc_leftSpriteSheet = npc.getLeftSpriteSheet()
#npc_rightSpriteSheet = npc.getRightSpriteSheet()
#npc_downSpriteSheet = npc.getDownSpriteSheet()
#npc_upSpriteSheet = npc.getUpSpriteSheet()
#npc_frame_index = 0
#npc_image = npc_leftSpriteSheet[npc_frame_index]

# Interaction variables
e_pressed = False
msg = ""


def checkForExit( event ):
	if event.type == QUIT:
		exit()

def renderNPC( npc, sprite ):
	global screen
	

def updateBackground( map_screen ):
	global screen
	screen.blit(map_screen.getImage(), (0,0))

def updateCharacter( player, sprite, image_to_change ):
	global image
	screen.blit(sprite, player.getPosition())
	image = sprite

# returns the first interactable block that is above, below, or the right or left of the player
def checkSurroundingBlocks( x, y, cmap ):
	if (x + 1) < cmap.getMaxX() and cmap.getRoom()[x+1][y].isInteractable :
		return cmap.getRoom()[x+1][y]
	elif (x - 1) >= 0  and cmap.getRoom()[x-1][y].isInteractable :
		return cmap.getRoom()[x-1][y]
	elif (y + 1) < cmap.getMaxY() and cmap.getRoom()[x][y+1].isInteractable :
		return cmap.getRoom()[x][y+1]
	elif (y - 1) >= 0  and cmap.getRoom()[x][y-1].isInteractable :
		return cmap.getRoom()[x][y-1]
	else:
		return None

def splitMessage( msg, char_limit ):
	msg_list = []
	if len(msg) <= char_limit:
		msg_list.append(msg)
		return msg_list
	num1 = 0
	num2 = char_limit
	for i in range( int(math.ceil(len(msg)/float(char_limit)))):
		if num2 > len(msg):
			num2  = len(msg)
		msg_list.append(msg[num1:num2])
		num1 += char_limit
		num2 += char_limit
	return msg_list


def displayMessage( msg ):
	text_size = 30
	close_text_size = 16
	x = 1280/4
	y = 960-960/4
	msg_list = splitMessage( msg, 35 )
	pygame.draw.rect(screen, (0,0,0), ((1280/4,960-960/4), (1280/2,960/2)) )
	close_font = pygame.font.SysFont("Arial", close_text_size)
	myfont = pygame.font.SysFont("Arial", text_size)
	size_multiplier = 1
	for m in msg_list:
		screen.blit(myfont.render(m, True, (255,255,255)), (x, y))
		y += text_size
	screen.blit(close_font.render('Press E to Close', True, (255,255,255)), (1280/2-30, 960-close_text_size)) 


def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False

def move( player, x, y, current_map, spritesheet, image ):
	new_x = player.getX()/BLOCK_SIZE_X + x/BLOCK_SIZE_X
	new_y = player.getY()/BLOCK_SIZE_Y + y/BLOCK_SIZE_Y
	nextBlock = current_map.getRoom()[new_x][new_y]
	# check to see if next block is a wall
	if nextBlock.isWall:
		return
	# check to see if player needs to be transitioned to another room
	for spriteframe in spritesheet:
		x_add = x/len(spritesheet) 
		y_add = y/len(spritesheet) 
		player.setPosition( player.getX() + x_add, player.getY() + y_add )
		updateBackground(current_map)
		pygame.time.delay(70)
		updateCharacter(player,spriteframe, image)
		pygame.display.update()
	if nextBlock.hasTransition:
		#player.setPosition((nextBlock.getDestinationX() + 1)*BLOCK_SIZE_X, (nextBlock.getDestinationY() +1)*BLOCK_SIZE_Y)
		player.setPosition((nextBlock.getDestinationX())*BLOCK_SIZE_X, (nextBlock.getDestinationY())*BLOCK_SIZE_Y)
		current_map.makeActive(False)
		nextBlock.getDestinationRoom().makeActive(True)
		updateBackground( nextBlock.getDestinationRoom() )
		updateCharacter(player, spritesheet[0], image)
		pygame.display.update()
	#	return
	# set up block states
	if player.isPlayer:
		player.getCurrentBlock().setChar(False)
		nextBlock.setChar(True, player)
	

while True:

	#event = pygame.event.wait()
	interact_block = None
#	print 'in top of loop'
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	pressed_keys = pygame.key.get_pressed()
	current_map = level_1_map.getActiveRoom()
	# Left Arrow or A movement
	if pressed_keys[K_LEFT] or pressed_keys[K_a]:
		move( player, -BLOCK_SIZE_X, 0, current_map, leftSpriteSheet, image )
	#	move( -BLOCK_SIZE_X, 0, current_map, leftSpriteSheet )
	## Right Arrow or D movement
	elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
		move( player, BLOCK_SIZE_X, 0, current_map, rightSpriteSheet, image)
	#	move( BLOCK_SIZE_X, 0, current_map, rightSpriteSheet )
	# Up Arrow or W movement
	elif pressed_keys[K_UP] or pressed_keys[K_w]:
		move( player, 0, -BLOCK_SIZE_Y , current_map, upSpriteSheet, image )
	#	move( 0, -BLOCK_SIZE_Y , current_map, leftSpriteSheet )
	# Down Arrow or S movement
	elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
		move( player, 0, BLOCK_SIZE_Y , current_map, downSpriteSheet, image )
	#	move( 0, BLOCK_SIZE_Y , current_map, downSpriteSheet )
	#if event.type == KEYDOWN and not e_pressed:
	#	if event.key == K_LEFT:
	#		move( player, -BLOCK_SIZE_X, 0, current_map, leftSpriteSheet, image )
	#		move( npc, -BLOCK_SIZE_X, 0, current_map, npc_leftSpriteSheet, npc_image )
	#	elif event.key == K_RIGHT:
	#		move( player, BLOCK_SIZE_X, 0, current_map, rightSpriteSheet, image)
	#		move( npc, BLOCK_SIZE_X, 0, current_map, npc_rightSpriteSheet, npc_image)
	#	elif event.key == K_UP:
	#		move( player, 0, -BLOCK_SIZE_Y , current_map, upSpriteSheet, image )
	#		move( npc, 0, -BLOCK_SIZE_Y , current_map, npc_upSpriteSheet, npc_image )
	#	elif event.key == K_DOWN:
	#		move( player, 0, BLOCK_SIZE_Y , current_map, downSpriteSheet, image )
	#		move( npc, 0, BLOCK_SIZE_Y , current_map, npc_downSpriteSheet, npc_image )

#	print 'in mid of loop'	
	
	# Check for interaction key press
	if e_pressed:
	#	print 'in e_pressed true'
		event = pygame.event.wait()
		checkForExit(event)
		if event.type == KEYDOWN:
			if event.key == K_e:
				current_map = level_1_map.getActiveRoom().reloadRoomImage()
				e_pressed = False
	else:
	#	print 'in e_pressed false'
		event = pygame.event.wait()
		checkForExit(event)
		if event.type == KEYDOWN:
			if event.key == K_e:
				interact_block = checkSurroundingBlocks(player.getCurrentBlock().getX(), player.getCurrentBlock().getY(), current_map)
				if interact_block != None:
					msg = interact_block.getMessage()
					e_pressed = True
				#	displayMessage( 'Thomp thomp is a BADASS')
		#pygame.draw.rect(screen, (0,0,0), ((1280/4,960-960/4), (1280/2,960/2)) )
		#myfont = pygame.font.SysFont("Arial", 30)
		#label = myfont.render("Test", 1, (255,255,255))
		#screen.blit(label, (1280/4, 960-960/4))
		#pygame.display.update()
		#pygame.time.delay(1000)

	updateBackground(current_map)
	updateCharacter(player, image, image)
#	updateCharacter(npc, npc_image, npc_image)
	if( e_pressed ):
		displayMessage( msg )
		#pygame.draw.rect(current_map.getImage(), (0,0,0), ((1280/4,960-960/4), (1280/2,960/2)) )
		#myfont = pygame.font.SysFont("Arial", 30)
		#label = myfont.render('Test', 1, (255,255,255))
		#end_label = endlabel_font.render('Press E', 1, (255,255,255))
		#screen.blit(label, (1280/4, 960-960/4))
		#screen.blit(end_label, (1280/2 , 960-16))
		
	#screen.blit(current_map.getImage(), (0,0))
	#screen.blit(image, player.getPosition()) 
	
	pygame.display.update()
