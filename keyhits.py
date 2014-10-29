#guiInput
import threading
import termios, fcntl, sys, os
import threading

class KeyHits(threading.Thread):
    gui = 0
    def __init__(self, guiArg):
	threading.Thread.__init__(self)
	self.gui = guiArg
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
	except KeyboardInterrupt: sys.exit()
	finally:
	    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
	    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

    def processIn(self, char):
	if(char == 'w'):
		self.gui.keyUp()
	elif(char == 'a'):
		self.gui.keyLeft()
	elif(char == 's'):
		self.gui.keyDown()
	elif(char == 'd'):
		self.gui.keyRight()
	elif(char == 'p'):
		self.gui.keyPause()
	elif(char == 'r'):
		self.gui.keyReset()
