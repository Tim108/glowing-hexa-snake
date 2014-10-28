#Main
import threading
from menu import *
from input import *

menu = Menu()
input = Input()

menu.start()
input.start()

menu.join()
input.join()


