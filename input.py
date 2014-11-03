#catch input
from gui import *
from Queue import Queue
import threading
import RPi.GPIO as GPIO
import time

queue = Queue()

class InputProducer(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)	
	
		self.pins = [17,18,27,8,11,9,10,25,24,23,22]
		self.init_connection()

	def init_connection(self):
		GPIO.setwarnings(False)
	        GPIO.setmode(GPIO.BCM)
        	GPIO.setup(4, GPIO.IN)#valid bit

        	for p in self.pins:
	            GPIO.setup(p, GPIO.IN)#input bits


	def run(self):
	        while True:
        		GPIO.wait_for_edge(4,GPIO.RISING)

                	pinvalues = []
                	for p in self.pins:
                    		pinvalues.append(GPIO.input(p))

			queue.put(pinvalues)



class InputConsumer(threading.Thread):
    mygui = 0
    pins = [17,18,27,8,11,9,10,25,24,23,22]

    def __init__(self):
	threading.Thread.__init__(self)	
	

    def run(self):

	while True:
		val = queue.get()
		n,l = self.processinput(val)
		self.createEvent(n,l)

    def processinput(self, val):
	action = ""
	location = ""

	for i in range(3,11): #Number (location) that's being sent
		location = location + str(val[i])
	print "bit array for location = " + str(int(location, 2))
	location = int(location, 2) #Convert the binary string to int

	for i in range(0,3): #What the number represents
 		action = action + str(val[i])
	print "bit array for action = " + str(int(action, 2))
	action = int(action, 2) #Convert the binary string to int

	return action, location

    def createEvent(self, n, l):
	if(n == 4 or n == 2 or n == 6 or n == 1 or n == 3): #showScore, candy, addSnake, delSnake, gameOver
		e = pygame.event.Event(USEREVENT, action=n, location=l)
		pygame.event.post(e)

	else: print str(n) + " is no valid input"

if __name__ == "__main__":
	prod = InputProducer()
	prod.init_connection()

	cons = InputConsumer()

	prod.start()
	cons.start()
