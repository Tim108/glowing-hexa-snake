#menu gui
from output import *
import threading

class Menu(threading.Thread):
    def run(self):
	i = 0
	while(i<20):
	    print '{}{}'.format("menu " , i)
	    i = i+1

