#pregunta 6

from learntools.core import binder; binder.bind(globals())
from learntools.python.ex3 import *

def exactly_one_topping(ketchup, mustard, onion):
    return (int(ketchup) + int(mustard) + int(onion)) == 1
    pass

q6.check()