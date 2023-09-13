#pregunta 1

from learntools.core import binder; binder.bind(globals())
from learntools.python.ex3 import *

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

q1.check()