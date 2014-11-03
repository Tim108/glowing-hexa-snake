import threading
import termios, fcntl, sys, os
import RPi.GPIO as GPIO
import time

class Output(threading.Thread):
    def __init__(self, lock):
	self.lock = lock
	
	GPIO.setwarnings(False) 
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(14, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(2, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)

	self.reset()

    def reset(self):
	GPIO.output(14, GPIO.LOW)
	GPIO.output(15, GPIO.LOW)
	GPIO.output(2, GPIO.LOW)
	GPIO.output(3, GPIO.LOW)

    def up(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(3, GPIO.HIGH)
	self.lock.release()

    def down(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(14, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	self.lock.release()

    def left(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(15, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	self.lock.release()

    def right(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(14, GPIO.HIGH)
	GPIO.output(15, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	self.lock.release()

    def bPause(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(2, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	self.lock.release()

    def bReset(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(14, GPIO.HIGH)
	GPIO.output(2, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	self.lock.release()

    def bStart(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(15, GPIO.HIGH)
	GPIO.output(2, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	self.lock.release()

    def bExit(self):
	self.lock.acquire()
	self.reset()
	GPIO.output(14, GPIO.HIGH)
	GPIO.output(15, GPIO.HIGH)
	GPIO.output(2, GPIO.HIGH)
	GPIO.output(3, GPIO.HIGH)
	self.lock.release()

