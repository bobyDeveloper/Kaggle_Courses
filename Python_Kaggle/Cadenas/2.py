from learntools.core import binder; binder.bind(globals())
from learntools.python.ex6 import *

def is_valid_zip(zip_code):
    return len(zip_code) == 5 and zip_code.isdigit()

q1.check()