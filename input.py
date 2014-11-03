#catch input
from gui import *
import threading
import RPi.GPIO as GPIO

class Input(threading.Thread):
    mygui = 0
    pins = [17,18,27,22,23,24,25,10,9,11,8,7]
    def __init__(self, gui):
	threading.Thread.__init__(self)	
	
	self.myGui = gui

    def run(self):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.IN)#valid bit
        for p in self.pins:
            GPIO.setup(p, GPIO.IN)#input bits

        while(1):
	    GPIO.wait_for_edge(4,GPIO.RISING)
	    pinvalues = []
            for p in self.pins:
                pinvalues.append(GPIO.input(p))
            self.processinput(pinvalues)

    def processinput(self, pinvalues):
        action = ""
        location = ""

        for i in range(3,11): #Number (location) that's being sent
            location = location + str(pinvalues[i])
	print "bit array for location = " + location        
	location = int(location, 2) #Convert the binary string to int

        for i in range(0,3): #What the number represents
            action = action + str(pinvalues[i])
	print "bit array for action = " + action
	action = int(action, 2) #Convert the binary string to int

	self.createEvent(action, location)        

    def createEvent(self, n, l):
	if(n == 4 or n == 2 or n == 6 or n == 1 or n == 7): #showScore, candy, addSnake, delSnake, gameOver
		e = pygame.event.Event(USEREVENT, action=n, location=l)
		pygame.event.post(e)

	else: print str(n) + " is no valid input"
