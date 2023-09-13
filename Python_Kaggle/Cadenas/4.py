from learntools.core import binder; binder.bind(globals())
from learntools.python.ex6 import *

def multi_word_search(doc_list, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        indices = [i for i, doc in enumerate(doc_list) if keyword.lower() in doc.lower()]
        keyword_to_indices[keyword] = indices
    return keyword_to_indices

doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']

print(multi_word_search(doc_list, keywords))
