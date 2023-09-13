#pregunta 4

from learntools.core import binder; binder.bind(globals())
from learntools.python.ex3 import *

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number < 0

q4.check()