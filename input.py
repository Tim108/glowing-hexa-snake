#catch input
from menu import *
import threading

class Input(threading.Thread):
    def run(self):
	i = 0
	while(i<20):
	    print '{}{}'.format("input " , i)
	    i = i+1

