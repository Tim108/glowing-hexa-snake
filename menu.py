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

