#Main
import threading

class Output(threading.Thread):
    def __init__(self):
        execfile("output.py")
	self.Output.__init__()

    def run(self):
	self.Output.run()

class Menu(threading.Thread):
     def __init__(self, Output):
        execfile("menu.py")
	
     def run(self):
	self.MainMenu.__init__()

outputThread = Output()   
menuThread = Menu(outputThread)
outputThread.start()
menuThread.start()
outputThread.join()
menuThread.join()


