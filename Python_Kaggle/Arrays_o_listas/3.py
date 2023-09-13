from learntools.core import binder; binder.bind(globals())
from learntools.python.ex4 import *

def purple_shell(racers):

    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp
    pass


q3.check()