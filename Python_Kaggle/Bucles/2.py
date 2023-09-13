from learntools.core import binder; binder.bind(globals())
from learntools.python.ex5 import *

def elementwise_greater_than(L, thresh):
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res


q2.check()