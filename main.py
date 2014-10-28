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

class Input(threading.Thread):
    def __init__(self, MainMenu):
	execfile("input.py")
	self.Input.__init__()
    
    def run(self):
	self.Input.run()

outputThread = Output()   
menuThread = Menu(outputThread.Output)
inputThread = Input(menuThread.MainMenu)
outputThread.start()
menuThread.start()
inputThread.start()
outputThread.join()
menuThread.join()
inputThread.join()


