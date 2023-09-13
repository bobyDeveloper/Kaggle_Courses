from learntools.core import binder; binder.bind(globals())
from learntools.python.ex6 import *

a = ""
length = 0  
q0.a.check()

b = "it's ok"
length = 7
q0.b.check()

c = 'it\'s ok'
length = 7
q0.c.check()

d = """hey"""
length = 3
q0.d.check()

e = '\n'
length = len(e)  # Asignar el valor adecuado a 'length'
q0.e.check() 