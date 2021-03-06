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
    states = ['menu', 'highscores', 'inGame', 'pause', 'gameOver', 'drawSnake', 'drawCandy', 'deleteSnake']
    def __init__(self):
        threading.Thread.__init__(self)
	#Geef mee in welke state de gui is, dan weet die wat er getekend moet worden
	# de volgende states bestaan: 'menu', 'gameover', 'pause', 'highscores', 'inGame'
	self.guiState = Gui.states[0]
#	self.renderer = Renderer(self.guiState)

    def run(self):
        lock = threading.Lock()
        self.o = Output(lock)
#       thread.start_new_thread( o.up, () )
#       gui mag hier
#       Eerst een scherm maken
	
	#Teken het gehele scherm
        self.renderer = Renderer(self.o)
	self.renderer.start()
	print "24 kleine pindaatjes"
	self.renderer.join()
	#self.addSnake(45)

    #Input from fpga board
    def showScore(self, score):
        print "Your score is " + str(score)
	self.guiState = Gui.states[2]
	self.renderer.changeState(self.guiState, score)

    def candy(self, location):
	self.guiState = Gui.states[6]
	self.renderer.changeState(guiState, location)
        print "Candy discovered on tile " + str(location)

    def addSnake(self, location):
	print "banaantjes"
	self.guiState = Gui.states[5]
	print "1"
	self.renderer.changeState(self.guiState, location)
        print "Snake tile created at " + str(location)

    def delSnake(self, location):
	self.guiState = Gui.states[7]
	self.renderer.changeState(self.guiState, location)
        print "Snake tile deleted at " + str(location)

    def gameOver(self, score):
	try:
		self.guiState = Gui.states[4]
		self.renderer.changeState(self.guiState, score)
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
	self.guiState = Gui.states[3]
	self.renderer = Renderer(gui.states[3])

    def keyReset(self):
	print "Reset is pushed"
	self.o.bReset()

if __name__ == '__main__':
	gui = Gui()
