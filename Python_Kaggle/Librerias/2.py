from learntools.core import binder; binder.bind(globals())
from learntools.python.ex7 import *

from learntools.python import jimmy_slots

def prettify_graph(graph):

    raph.set_title("Results of 500 slot machine pulls")

    graph.set_ylim(bottom=0)

    graph.set_ylabel("Balance")

    ticks = graph.get_yticks()

    new_labels = ['${}'.format(int(amt)) for amt in ticks]

    graph.set_yticklabels(new_labels)
graph = jimmy_slots.get_graph()
graph


def best_items(racers):

    winner_item_counts = {}
    for i in range(len(racers)):
        racer = racers[i]
        if racer['finish'] == 1:
            for i in racer['items']:
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts