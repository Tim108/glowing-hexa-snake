#Main
import threading
from menu import *
from input import *

menu = Menu()
killInput = threading.Event()
input = Input(menu, killInput)

menu.start()
input.start()

print "at the joins"
menu.join()
print "menu joined"
killInput.set()
input.join()
print "input joined"

