import threading
import termios, fcntl, sys, os
import RPi.GPIO as GPIO
import time
import atexit

class Output(threading.Thread):
    def __init__(self, lock):
	self.lock = lock

	fd = sys.stdin.fileno()
    
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
    
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
 
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(8, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)

    def reset(self):
	self.lock.acquire()
	GPIO.output(8, GPIO.LOW)
	GPIO.output(10, GPIO.LOW)
	GPIO.output(3, GPIO.LOW)
	GPIO.output(5, GPIO.LOW)
	self.lock.release()

    def up(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(5, GPIO.HIGH)
	self.lock.release()

    def down(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	self.lock.release()

    def left(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(10, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	self.lock.release()

    def right(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	self.lock.release()

    def pause(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	self.lock.release()

    def bReset(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	self.lock.release()

    def bStart(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(10, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	self.lock.release()

    def bExit(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(5, GPIO.HIGH)
	GPIO.cleanup()
	self.lock.release()

atexit.register(GPIO.cleanup())
