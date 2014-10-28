import threading

class Output(threading.Thread):
    def run(self):
	i = 0
	while(i < 20):
	    print '{}{}'.format("output " , i)
	    i = i+1
