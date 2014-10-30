#gui
from output import *
from renderer import *
import threading
import thread
import time

import pygame

from pygame.locals import *
from pygame.color import Color

class Gui(threading.Thread):
    myInput = 0
    o = 0
    renderer = 0
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        lock = threading.Lock()
        self.o = Output(lock)
#       thread.start_new_thread( o.down, () )
#       thread.start_new_thread( o.up, () )
#       gui mag hier
#       Eerst een scherm maken
	self.renderer = Renderer(self)
	self.showScore(5)
	
    #Input from fpga board
    def showScore(self, score):
        print "Your score is " + str(score)
	self.renderer.printScore(score)

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
