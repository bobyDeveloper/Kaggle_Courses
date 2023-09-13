#pregunta 2

from learntools.core import binder; binder.bind(globals())
from learntools.python.ex3 import *

def to_smash(total_candies):
    total_candies=1 

to_smash(91)

def to_smash(total_candies):
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
to_smash(91)
to_smash(1)

q2.check()