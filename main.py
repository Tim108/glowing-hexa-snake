#Main
import threading
from menu import *
from input import *
from output import *

output = Output()
menu = Menu()
input = Input()

output.start()
menu.start()
input.start()

output.join()
menu.join()
input.join()


