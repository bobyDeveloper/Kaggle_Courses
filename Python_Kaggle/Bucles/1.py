from learntools.core import binder; binder.bind(globals())
from learntools.python.ex5 import *

def has_lucky_number(nums):

    return any([num % 7 == 0 for num in nums])

q1.check()