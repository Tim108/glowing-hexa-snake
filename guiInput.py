#guiInput
import sys

class guiIn(self, threading.Thread):
    gui = 0
    def __init__(self, menu):
	gui = menu

    def run(self):
	while(True):
	    char = sys.stdin.read(1)
	    print 'You pressed %s' % char
