import termios, fcntl, sys, os
import RPi.GPIO as GPIO 
import time

class Output(self):
    def __init__(self):

	fd = sys.stdin.fileno()

	oldterm = termios.tcgetattr(fd)
	newattr = termios.tcgetattr(fd)
	newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
	termios.tcsetattr(fd, termios.TCSANOW, newattr)

	oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
	fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(22, GPIO.OUT)
	GPIO.setup(23, GPIO.OUT)
	GPIO.setup(24, GPIO.OUT)

    def run(self):
	code = '-1'
	try:
	    while 1:
	        try:
	            c = sys.stdin.read(1)
	            print "Got character", c
		    if str(c) == 'w':
			code = '001'
			#GPIO.output(22, 1)
			time.sleep(0.1)
			#GPIO.output(22, 0)
			print 'snake ga naar boven!'
	   	    elif str(c)=='s':
			code = '010'
			#GPIO.output(23, GPIO.HIGH)
			time.sleep(0.1)
               		#GPIO.output(23, GPIO.LOW)
			print 'snake ga naar beneden!'
		    elif str(c)=='a':
		        code = '011'
			#GPIO.output(24, GPIO.HIGH)
               		time.sleep(0.1)
        	      	#GPIO.output(24, GPIO.LOW)
			print 'snake ga naar links!'
		    elif str(c)=='d':
			code = '100'
			#GPIO.output(22, GPIO.HIGH)
			#GPIO.output(23, GPIO.HIGH)
               		time.sleep(0.1)
               		#GPIO.output(22, GPIO.LOW)
			#GPIO.output(23, GPIO.LOW)
			print 'snake ga naar rechts!'
	   	    elif str(c)=='p':
			code = '101'
			#GPIO.output(22, GPIO.HIGH)
			#GPIO.output(24, GPIO.HIGH)
			time.sleep(0.1)
			#GPIO.output(24, GPIO.LOW)
			#GPIO.output(22, GPIO.LOW)
			print 'pauseer game!'
	   	    elif str(c)=='r':
			code = '000'
			#GPIO.output(23, GPIO.HIGH)
			#GPIO.output(24, GPIO.HIGH)
			time.sleep(0.1)
			#GPIO.output(23, GPIO.LOW)
			#GPIO.output(24, GPIO.LOW)
			print 'reset game!'
	  	    elif str(c)=='q':
			code='special'
			i=0
			while(i<100):
				GPIO.output(22, GPIO.HIGH)
				time.sleep(0.010)
				GPIO.output(22, GPIO.LOW)
				time.sleep(0.010)
	    			i = i+1
	   	    else:
			code='-1'
	   	
		    if code!='-1':
			if code[0]=='1':
				GPIO.output(22, GPIO.HIGH)
			else:
				GPIO.output(22, GPIO.LOW)
			if code[1]=='1':
				GPIO.output(23, GPIO.HIGH)
			else:
				GPIO.output(23, GPIO.LOW)
			if code[2]=='1':
				GPIO.output(24, GPIO.HIGH)
			else:
				GPIO.output(24, GPIO.LOW)
			print code
			code = '-1'
       	
		except IOError: pass
		except KeyboardInterrupt: GPIO.cleanup()
	finally:
   		termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
  		fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
