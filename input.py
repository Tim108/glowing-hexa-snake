#catch input
from gui import *
import threading
import RPi.GPIO as GPIO

class Input(threading.Thread):
    mygui = 0
    pins = [11,12,13,15,16,18,22,19,21,23,24,26]
    
    def __init__(self, gui):
	threading.Thread.__init__(self)	
	
	self.myGui = gui

    def run(self):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
        GPIO.setup(7, GPIO.IN)#valid bit
        for p in self.pins:
            GPIO.setup(p, GPIO.IN)#input bits

        gotIt = False
        while(GPIO in globals()):
            if (GPIO.input(7) and gotIt == False):
                pinvalues = []
                gotIt = True
                for p in self.pins:
                    pinvalues.append(GPIO.input(p))
                self.processinput(pinvalues)
            else:
                gotIt = False

    def processinput(self, pinvalues):
        action = ""
        location = ""

        for i in range(3,11): #Number (location) that's being sent
            location = location + str(pinvalues[i])
        
	location = int(location, 2) #Convert the binary string to int

        for i in range(0,2): #What the number represents
            action = action + str(pinvalues[i])
	print str(action) + " dingetjes en banaantjes "
	self.doAction(action, location)        

    def doAction(self, n, l):
	actions = {00 : None,
			1 : self.myGui.showScore,
        	       	2 : self.myGui.candy,
               		3 : self.myGui.addSnake,
              	 	4 : self.myGui.delSnake,
			7 : self.myGui.gameOver,
	}

	actions[1](l)

