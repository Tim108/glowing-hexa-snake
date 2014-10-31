#catch input
from gui import *
import threading
import RPi.GPIO as GPIO

class Input(threading.Thread):
    mygui = 0
    pins2 = [11,12,13,15,16,18,22,19,21,23,24,26]
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
 	    print "time = " + str(GPIO.input(4))
	    GPIO.wait_for_edge(4,GPIO.RISING)
	    print "%.20f" % time.time()
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

	self.doAction(action, location)        

    def doAction(self, n, l):
	if(n == 1): self.myGui.showScore(l)
	elif(n == 2): self.myGui.candy(l)
	elif(n == 3): self.myGui.addSnake(l)
	elif(n == 4): self.myGui.delSnake(l)
	elif(n == 7): self.myGui.gameOver(l)
	else: print str(n) + "is no valid input"
