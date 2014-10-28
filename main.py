#Main
import threading
from menu import *
from input import *

menu = Menu()
input = Input()

menu.start()
input.start()

print "at the joins"
menu.join()
print "menu joined"
input.join()
print "input joined"


