#gui
from output import *
from renderer import *
import threading
import thread
import time
import math

import pygame

from pygame.locals import *
from pygame.color import Color

class Gui(threading.Thread):
    myInput = 0
    o = 0
    guiState = 'menu'
    renderer = 0
    states = ['menu', 'highscores', 'inGame', 'pause', 'gameOver']
    def __init__(self):
        threading.Thread.__init__(self)
	#Geef mee in welke state de gui is, dan weet die wat er getekend moet worden
	# de volgende states bestaan: 'menu', 'gameover', 'pause', 'highscores', 'inGame'
	self.guiState = Gui.states[0]
#	self.renderer = Renderer(self.guiState)

    def run(self):
        lock = threading.Lock()
        self.o = Output(lock)
#       thread.start_new_thread( o.down, () )
#       thread.start_new_thread( o.up, () )
#       gui mag hier
#       Eerst een scherm maken
	
	#Teken het gehele scherm
	self.renderer = Renderer(self.guiState)

    def toXY(self, i):
	x = i % 15
	y = math.floor(i/15)
	return (x,y)
	
    #Input from fpga board
    def showScore(self, score):
        print "Your score is " + str(score)
	self.guiState = Gui.states[2]
	self.renderer = Renderer(self.guiState)
	self.renderer.printScore(score)

    def candy(self, location):
	self.guiState = Gui.states[2]
	location = self.toXY(location)
	self.renderer = Renderer(self.guiState)
	self.renderer.drawCandy(location)
        print "Candy discovered on tile " + str(location)

    def addSnake(self, location):
	self.guiState = Gui.states[2]
	location = self.toXY(location)
	self.renderer = Renderer(self.guiState)
	self.renderer.drawSnake(location)
        print "Snake tile created at " + str(location)

    def delSnake(self, location):
	self.guiState = Gui.states[2]
	location = self.toXY(location)
	self.renderer = Renderer(self.guiState)
	self.renderer.deleteSnake(location)
        print "Snake tile deleted at " + str(location)

    def gameOver(self, score):
	try:
		self.guiState = Gui.states[4]
		self.renderer = Renderer(self.guiState)
		self.renderer.drawGameOverOverlay()
	except: print "stuk"
        print "GameOver and we don't care about the score"

    #Input from keyboard
    def keyUp(self):
	print "Up is pushed"
	self.o.up()

    def keyLeft(self):
	print "Left is pushed"
	self.o.left()

    def keyDown(self):
	print "Down is pushed"
	self.o.down()

    def keyRight(self):
	print "Right is pushed"
	self.o.right()

    def keyPause(self):
	print "Pause is pushed"
	self.o.bPause()

    def keyReset(self):
	print "Reset is pushed"
	self.o.bReset()
