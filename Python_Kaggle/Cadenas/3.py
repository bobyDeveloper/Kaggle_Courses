from learntools.core import binder; binder.bind(globals())
from learntools.python.ex6 import *

def word_search(doc_list, keyword):
    indices = [] 
    for i, doc in enumerate(doc_list):

        tokens = doc.split()
       
        normalized = [token.rstrip('.,').lower() for token in tokens]

        if keyword.lower() in normalized:
            indices.append(i)
    return indices


q2.check()