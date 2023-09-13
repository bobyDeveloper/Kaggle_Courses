from learntools.core import binder; binder.bind(globals())
from learntools.python.ex5 import *

def menu_is_boring(meals):

    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
q3.check()