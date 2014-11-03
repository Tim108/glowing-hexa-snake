#Main
import threading
from gui import *
from input import *
from keyhits import *

#Initialize threads
gui = Gui()
gui.daemon = True
inputProd = InputProducer()
inputProd.daemon = True
inputCons = InputConsumer()
inputCons.daemon = True
keyhits = KeyHits(gui)
keyhits.daemon = True
#Start threads
gui.start()
inputProd.start()
inputCons.start()
keyhits.start()
#Wait for gui to finish
try:
    gui.join()
except KeyboardInterrupt: sys.exit()
print "Main terminated"

