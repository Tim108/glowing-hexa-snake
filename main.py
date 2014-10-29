#Main
import threading
from gui import *
from input import *
from keyhits import *

#Initialize threads
gui = Gui()
input = Input(gui)
input.daemon = True
keyhits = KeyHits(gui)
keyhits.daemon = True
#Start threads
gui.start()
input.start()
keyhits.start()
#Wait for gui to finish
gui.join()
print "Main terminated"

