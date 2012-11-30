#! /usr/bin/env python
"""
A library used to calculate the Shapley value of a game.
"""

from __future__ import division
from math import factorial
from itertools import permutations

class cooperative_game():
    def __init__(self,coalition_dictionary):
        self.players=[eval(e)[0] for e in coalition_dictionary if len(eval(e))==1]
    def Shapley_Calculation(self):
        shapley_table={}
        for e in self.players:
            shapley_table[e]=0
        for e in permutations(self.players):
            for a in e:
                shapley_table[a]+=self.coalition_dictionary... #Can't figure it out...




