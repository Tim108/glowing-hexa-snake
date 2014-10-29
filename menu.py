#menu gui
from output import *
import threading
import thread
import time

class Menu(threading.Thread):

    def __init__(self):
	threading.Thread.__init__(self)

    def run(self):
	time.sleep(1)
	lock = threading.Lock()
	o = Output(lock)
	thread.start_new_thread(o.down, ())
	thread.start_new_thread(o.up, ())
	i = 0
	while(i<20):
	    print '{}{}'.format("menu " , i)
	    i = i+1

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
