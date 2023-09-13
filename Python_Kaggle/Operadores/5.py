#pregunta 5

from learntools.core import binder; binder.bind(globals())
from learntools.python.ex3 import *

def onionless(ketchup, mustard, onion):

    return not onion

def wants_all_toppings(ketchup, mustard, onion):
    return ketchup and mustard and onion
    pass

q5.a.check()

def wants_plain_hotdog(ketchup, mustard, onion):
    return not ketchup and not mustard and not onion
    pass


q5.b.check()

def exactly_one_sauce(ketchup, mustard, onion):
    return (ketchup and not mustard) or (mustard and not ketchup)
    pass

q5.c.check()