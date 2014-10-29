import threading
import termios, fcntl, sys, os
import RPi.GPIO as GPIO
import time

class Output(threading.Thread):
    def __init__(self, lock):
	self.lock = lock
	
	GPIO.setwarnings(False) 
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(8, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)

    def reset(self):
	GPIO.output(8, GPIO.LOW)
	GPIO.output(10, GPIO.LOW)
	GPIO.output(3, GPIO.LOW)
	GPIO.output(5, GPIO.LOW)

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
	self.lock.release()

