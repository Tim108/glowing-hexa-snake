#gui
from output import *
import threading
import thread
import time

import pygame

from pygame.locals import *
from pygame.color import Color

class Gui(threading.Thread):
    myInput = 0

    def __init__(self):
        threading.Thread.__init__(self)

    def initInput(self, input):
        self.myInput = input

    def run(self):
        time.sleep(1)
        lock = threading.Lock()
        o = Output(lock)
#       thread.start_new_thread( o.down, () )
#       thread.start_new_thread( o.up, () )
#       gui mag hier
#       Eerst een scherm maken
#	self.display = pygame.display.set_mode((640, 480), pygame.HWSURFACE|pygame.DOUBLEBUF)
#	self.initializeScreen()
#	pygame.display.update()

#    def initializeScreen(self):
#	pygame.display.init()

	pygame.init()

	size = width, height = 640, 480
	black = 0, 0, 0

	screen = pygame.display.set_mode(size)

	while(True):
	    for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    sys.exit()
	    
	    screen.fill(black)
	    pygame.display.flip()

    #Input from fpga board
    def showScore(self, score):
        print "Your score is " + str(score)

    def candy(self, location):
        print "Candy discovered on tile " + str(location)

    def addSnake(self, location):
        print "Snake tile created at " + str(location)

    def delSnake(self, location):
        print "Snake tile deleted at " + str(location)

    def gameOver(self, score):
        print "GameOver and we don't care about the score"

    #Input from keyboard
    def keyUp(self):
	print "Up is pushed"

    def keyLeft(self):
	print "Left is pushed"

    def keyDown(self):
	print "Down is pushed"

    def keyRight(self):
	print "Right is pushed"

    def keyPause(self):
	print "Pause is pushed"

    def keyReset(self):
	print "Reset is pushed"
