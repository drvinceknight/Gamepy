#!/usr/bin/env python
import copy


class Player():
    """
    Class for the general player in a matching game
    """
    def __init__(self, name, preferences):
        self.free = True
        self.partner = False
        self.preferences = preferences
        self.name = name


class Suitor(Player):
    """
    Class for the suitors (men) in a matching game.
    """

    def propose(self):
        """
        Method that returns top reviewer's name from list of preferences.
        """
        return self.preferences[0]


class Reviewer(Player):
    """
    Class for the reviewers (women) in a matching game.
    """
    def accept_proposal(self, suitor):
        """
        Method that returns True or False depending on whether a potential suitor is still in the preference list.
        """
        if suitor.name in self.preferences:
            return True
        return False


def Gale_Shapley_algorithm(strs, str_preferences, rvwrs, rvwr_preferences):
    """
    Algorithm to run the extended Gale Shapley algorithm as described in Irving 1994
    """
    """
    Creating copies of the inputs so that they can be manipulated without changing outputs.
    """
    suitors = copy.deepcopy(strs)
    suitor_preferences = copy.deepcopy(str_preferences)
    reviewers = copy.deepcopy(rvwrs)
    reviewer_preferences = copy.deepcopy(rvwr_preferences)
    """
    Initialisation, create dictionaries with keys the names of the players and values the players
    """
    suitors = dict([[s, Suitor(s, suitor_preferences[s])] for s in suitors])
    reviewers = dict([[r, Reviewer(r, reviewer_preferences[r])] for r in reviewers])
    # Iterate over free suitors
    while len([e for e in suitors if suitors[e].free]) > 0:
        # Pick a free suitor:
        s = suitors[[e for e in suitors if suitors[e].free][0]]
        # Identify s top reviewer:
        r = reviewers[s.propose()]
        # Check if s is in r list
        if r.accept_proposal(s):
            # If r already had a partner break partnership
            if not r.free:
                r.partner.free = True
                r.partner.partner = False
            # Set r and s free to False and set partners
            s.free = False
            s.partner = r
            r.free = False
            r.partner = s
            # Remove succesors of s from r list:
            r.preferences = r.preferences[:r.preferences.index(s.name)]
        # Remove r from s list:
        s.preferences.remove(r.name)
    return dict([[s, suitors[s].partner.name] for s in suitors])


class Matching_Game():
    """
    Class for a matching game.
    """
    def __init__(self, suitor_preferences, reviewer_preferences):
        """
        Initialise
        """
        self.suitor_preferences = suitor_preferences
        self.reviewer_preferences = reviewer_preferences
        self.suitors = sorted(suitor_preferences.keys())
        self.reviewers = sorted(reviewer_preferences.keys())

    def solve(self):
        """
        Apply the Extended Gale Shapley Algorithm as described in Irving 1994
        """
        self.stable_matching = Gale_Shapley_algorithm(self.suitors, self.suitor_preferences, self.reviewers, self.reviewer_preferences)

    def invert_solve(self):
        """
        Apply solving algorithm but swap suitors and reviewers
        """
        self.inverted_stable_matching = Gale_Shapley_algorithm(self.reviewers, self.reviewer_preferences, self.suitors, self.suitor_preferences)


if __name__ == "__main__":
    """
    Here is some code that runs the library as a program if run at the cl. If no arguments are passed it calculates the matching for a short example given at the end of this file. If a csv file is passed as an argument it solves the matching game described in the csv file.
    """
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
                print "\t", game_test.stable_matching
                print "Inverted stable matching:"
                print "\t", game_test.inverted_stable_matching
            else:
                sys.exit("Passed argument must be a csv file.")

    else:
        suitrs = ["J", "K", "L", "M"]
        reviewrs = ["A", "B", "C", "D"]
        suitr_pref = {'J': ['A', 'D', 'C', 'B'], 'K': ['A', 'B', 'C', 'D'], 'L': ['B', 'D', 'C', 'A'], 'M': ['C', 'A', 'B', 'D']}
        reviewr_pref = {'A': ['L', 'J', 'K', 'M'], 'B': ['J', 'M', 'L', 'K'], 'C': ['K', 'M', 'L', 'J'], 'D': ['M', 'K', 'J', 'L']}

        game_test = Matching_Game(suitr_pref, reviewr_pref)
        game_test.solve()
        print game_test.stable_matching
        game_test.invert_solve()
        print game_test.inverted_stable_matching
