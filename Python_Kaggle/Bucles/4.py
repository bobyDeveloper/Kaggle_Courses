from learntools.core import binder; binder.bind(globals())
from learntools.python.ex5 import *

play_slot_machine()

def estimate_average_slot_payout(n_runs):

    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    avg_payout = sum(payouts) / n_runs
    return avg_payout

pass