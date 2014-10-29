#catch input
from menu import *
import threading

class Input(threading.Thread):
    stop = 0
    myMenu = 0
    pins = [11,12,13,15,16,18,22,19,21,23,24,26]
    
    def __init__(self, menu, stopArg):
	threading.Thread.__init__(self)	
	
	self.stop = stopArg
	self.myMenu = menu

	GPIO.setmode(GPIO.BCM)
        GPIO.setup(7, GPIO.IN)#valid bit
        for p in self.pins:
            GPIO.setup(p, GPIO.IN)#input bits

    def run(self):
        gotIt = False
        while(not self.stop.is_set()):
            x = GPIO.input(7)
            if (x == 1):
                pinvalues = []
                gotIt = True
                for p in pins:
                    pinvalues.extend(GPIO.input(p))
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

        actions[action](location)

actions = {1 : Menu.showScore,
                2 : Menu.candy,
                3 : Menu.addSnake,
                4 : Menu.delSnake,
                7 : Menu.gameOver,
}


