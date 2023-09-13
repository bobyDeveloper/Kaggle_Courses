from learntools.core import binder; binder.bind(globals())
from learntools.python.ex4 import *

def fashionably_late(arrivals, name):

    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1
    pass


q5.check()