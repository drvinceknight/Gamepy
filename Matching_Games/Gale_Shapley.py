#!/usr/bin/env python
import copy

guyprefers = {'A': ['Y', 'X', 'Z'], 'B': ['C', 'B', 'A'], 'C': ['X', 'Z', 'Y']}
galpreferes = {'X': ['B', 'A', 'C'], 'Y': ['C', 'B', 'A'], 'Z': ['A', 'C', 'B']}

guyprefers = {'J': ['A', 'D', 'C', 'B'], 'K': ['A', 'B', 'C', 'D'], 'L': ['B', 'D', 'C', 'A'], 'M': ['C', 'A', 'B', 'D']}
galprefers = {'A': ['L', 'J', 'K', 'M'], 'B': ['J', 'M', 'L', 'K'], 'C': ['K', 'M', 'L', 'J'], 'D': ['M', 'K', 'J', 'L']}


def matchmaker():
    guysfree = guys[:]
    engaged = {}
    guyprefers2 = copy.deepcopy(guyprefers)
    galprefers2 = copy.deepcopy(galprefers)
    while guysfree:
        guy = guysfree.pop(0)
        guyslist = guyprefers2[guy]
        gal = guyslist.pop(0)
        fiance = engaged.get(gal)
        if not fiance:
            # She's free
            engaged[gal] = guy
        else:
            # The bounder proposes to an engaged lass!
            galslist = galprefers2[gal]
            if galslist.index(fiance) > galslist.index(guy):
                # She prefers new guy
                engaged[gal] = guy
                if guyprefers2[fiance]:
                    # Ex has more girls to try
                    guysfree.append(fiance)
            else:
                # She is faithful to old fiance
                if guyslist:
                    # Look again
                    guysfree.append(guy)
    return engaged


def matchmaker(suitors, reviewers, suitor_preferences, reviewer_preferences):
    available_suitors = suitors[:]
    engaged = {}
    suitor_preferences_copy = copy.deepcopy(suitor_preferences)
    reviewer_preferences_copy = copy.deepcopy(reviewer_preferences)
    while avilable_suitors:
        suitors = availablesuitors.pop(0)
        guyslist = guyprefers2[guy]
        gal = guyslist.pop(0)
        fiance = engaged.get(gal)
        if not fiance:
            # She's free
            engaged[gal] = guy
        else:
            # The bounder proposes to an engaged lass!
            galslist = galprefers2[gal]
            if galslist.index(fiance) > galslist.index(guy):
                # She prefers new guy
                engaged[gal] = guy
                if guyprefers2[fiance]:
                    # Ex has more girls to try
                    guysfree.append(fiance)
            else:
                # She is faithful to old fiance
                if guyslist:
                    # Look again
                    guysfree.append(guy)
    return engaged

class Matching_Game():
    """
    Class for a matching game.
    """
    def __init__(self, suitors_preference, reviewer_preferences):
        self.suitors_preferences = suitor_preferences
        self.reviewers_preferences = reviewer_preferences
        self.suitors = sorted(suitor_preferences.keys())
        self.reviewers = sorted(reviewer_preferences.keys())
