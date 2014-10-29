#guiInput
import threading
import termios, fcntl, sys, os

class guiIn():
    gui = 0
    def __init__(self):
	#gui = menu
	self.run()

    def run(self):
	fd = sys.stdin.fileno()

	oldterm = termios.tcgetattr(fd)
	newattr = termios.tcgetattr(fd)
	newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
	termios.tcsetattr(fd, termios.TCSANOW, newattr)

	oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
	fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
	try:
		print "herman"
		while(True):
		    try:
		        char = sys.stdin.read(1)
		        self.processIn(char)
		    except IOError: pass
		    except KeyboardInterrupt: pass
        except KeyboardInterrupt: pass
	finally:
	    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
	    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

    def processIn(self, char):
	if(char == 'w'):
		print "Go up"
	elif(char == 'a'):
		print "Go left"
	elif(char == 's'):
		print "Go down"
	elif(char == 'd'):
		print "Go right"
	elif(char == 'p'):
		print "Pause"
	elif(char == 'r'):
		print "Reset"
    
guiIn()
