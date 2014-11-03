import RPi.GPIO as GPIO
from time import sleep
VARIABLE_NAME = 14

if __name__ == "__main__":
 	GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(14, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(2, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)

	GPIO.output(15, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)

	print("dingen")
   	pins = [17,18,27,8,11,9,10,25,24,23,22]
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.IN)#valid bit
        for p in pins:
            GPIO.setup(p, GPIO.IN)#input bits
	print "setup..."
        while True:
	    GPIO.wait_for_edge(4,GPIO.RISING)
            pinvalues = []
            for p in pins:
                pinvalues.append(GPIO.input(p))
	    print pinvalues
	    sleep(0.25)
