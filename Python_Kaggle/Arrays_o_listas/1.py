from learntools.core import binder; binder.bind(globals())
from learntools.python.ex4 import *

def select_second(L):
    if len(L) < 2:
        return None
    return L[1]
    pass

q1.check()