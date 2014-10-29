#Main
import threading
from gui import *
from input import *

gui = Gui()
input = Input(gui)
input.daemon = True

gui.start()
input.start()

gui.join()
print "Main terminated"

