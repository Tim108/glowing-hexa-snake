#catch input
from menu import *
import threading

class Input(threading.Thread):
    pins = [11,12,13,15,16,18,22,19,21,23,24,26]

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(7, GPIO.IN)#valid bit
        for p in pins:
            GPIO.setup(p, GPIO.IN)#input bits

    def run(self):
        gotIt = false
        while(true):
            x = GPIO.input(7)
            if (x == 1):
                pinvalues = []
                gotIt = true
                for p in pins:
                    pinvalues.extend(GPIO.input(p))
                self.processinput(pinvalues)
            else:
                gotIt = false

    def processinput(self, pinvalues):
        action = ""
        location = ""

        for i in range(3,11) #Number (location) that's being sent
            location = location + str(pinvalues[i]
        location = int(location, 2) #Convert the binary string to int

        for i in range(0,2): #What the number represents
            action = action + str(pinvalues[i])

        actions[action](location)

actions = {1 : menuI.showScore,
                2 : menuI.candy,
                3 : addSnake,
                4 : delSnake,
                7 : gameOver,
}


