#Segunda pregunta

from learntools.core import binder; binder.bind(globals())
from learntools.python.ex1 import *

a = [1, 2, 3]
b = [3, 2, 1]
q2.store_original_ids()

temp = a
a = b
b = temp

q2.check()