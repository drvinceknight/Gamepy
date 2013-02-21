#!/usr/bin/env python
import copy


def Gale_Shapley_algorithm(guys, guyprefers, galprefers):
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


class Matching_Game():
    """
    Class for a matching game.
    """
    def __init__(self, suitor_preferences, reviewer_preferences):
        self.suitor_preferences = suitor_preferences
        self.reviewer_preferences = reviewer_preferences
        self.suitors = sorted(suitor_preferences.keys())
        self.reviewers = sorted(reviewer_preferences.keys())

    def solve(self):
        self.stable_matching = Gale_Shapley_algorithm(self.suitors, self.suitor_preferences, self.reviewer_preferences)

    def invert_solve(self):
        self.inverted_stable_matching = Gale_Shapley_algorithm(self.reviewers, self.reviewer_preferences, self.suitor_preferences)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
            if sys.argv[1][-4:] == ".csv":
                import csv
                outfile = open(sys.argv[1], "rb")
                raw_input = csv.reader(outfile)
                raw_input = [row for row in raw_input]
                outfile.close()

                number_of_suitors = raw_input.index([])
                suitors = [row[0] for row in raw_input[:number_of_suitors]]
                suitor_preferences = {}
                for e in raw_input[:number_of_suitors]:
                    suitor_preferences[e[0]] = e[1:]
                reviewers = [row[0] for row in raw_input[number_of_suitors + 1:]]
                reviewer_preferences = {}
                for e in raw_input[number_of_suitors + 1:]:
                    reviewer_preferences[e[0]] = e[1:]

                game_test = Matching_Game(suitor_preferences, reviewer_preferences)
                game_test.solve()
                game_test.invert_solve()
                print "Stable matching:"
                print "\t",game_test.stable_matching
                print "Inverted stable matching:"
                print "\t",game_test.inverted_stable_matching
            else:
                sys.exit("Passed argument must be a csv file.")

    else:
        guyprefers = {'J': ['A', 'D', 'C', 'B'], 'K': ['A', 'B', 'C', 'D'], 'L': ['B', 'D', 'C', 'A'], 'M': ['C', 'A', 'B', 'D']}
        galprefers = {'A': ['L', 'J', 'K', 'M'], 'B': ['J', 'M', 'L', 'K'], 'C': ['K', 'M', 'L', 'J'], 'D': ['M', 'K', 'J', 'L']}

        game_test = Matching_Game(guyprefers, galprefers)
        game_test.solve()
        print game_test.stable_matching
        game_test.invert_solve()
        print game_test.inverted_stable_matching
