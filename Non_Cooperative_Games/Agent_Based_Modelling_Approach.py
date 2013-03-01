"""
Algorithm from 'Game Theory Evolving'
"""
from __future__ import division
import copy
import random

# Need Individuals
"""
Define class that has attributes:
- Strategy
- Payoff
"""

# Let me try to code a program that solves matching pennies game...

"""
- Create population of players,
- Give them random strategies? (Or pure strategies?)
- Choose number of rounds per generation, play those rounds keeping everyone's core
- Once rounds are finished, calculate number of agents that will die due to
death rate
- Until those many agents die, kill worst agent and let best agent replicate with mutation probability mu. Mutation here is probability of picking a new strategy.
- Keep repeating above until number of generations have been created
"""


class Agent():
    """
    An agent class
    """
    def __init__(self, strategy):
        self.strategy = strategy
        self.utility = 0


def kill_one_agent_with_given_utility(agents, utility):
    number_of_agents = len(agents)
    k = 0
    while len(agents) == number_of_agents:
        if agents[k].utility == utility:
            del agents[k]
        k += 1


def reproduce_one_agent_with_given_utility(agents, utility, mutation_rate, strategies):
    number_of_agents = len(agents)
    k = 0
    while len(agents) == number_of_agents:
        if agents[k].utility == utility:
            agents.append(copy.deepcopy(agents[k]))
            if random.random() < mutation_rate:
                agents[-1].strategy = random.choice(strategies)
        k += 1


def return_current_strategy_distribution(agents, strategies):
        # Count results:
        frequencies = []
        for s in strategies:
            frequencies.append(0)
            for e in agents:
                if e.strategy == s:
                    frequencies[-1] += 1
        return [e / len(agents) for e in frequencies]


class ABM():
    """
    The model
    """
    def __init__(self, number_of_agents, generations, rounds_per_generation, death_rate, mutation_rate, row_matrix, col_matrix):
        self.number_of_agents = number_of_agents
        self.generations = generations
        self.rounds_per_generation = rounds_per_generation
        self.death_rate = death_rate
        self.number_of_deaths_per_generation = int(number_of_agents * death_rate)
        self.mutation_rate = mutation_rate
        self.row_strategies = range(len(row_matrix))
        self.col_strategies = range(len(col_matrix))
        self.row_agents = [Agent(random.choice(self.row_strategies)) for e in range(number_of_agents)]
        self.col_agents = [Agent(random.choice(self.col_strategies)) for e in range(number_of_agents)]
        self.row_matrix = row_matrix
        self.col_matrix = col_matrix

    def play_tournament(self):
        random.shuffle(self.col_agents)
        for i in range(self.number_of_agents):
            self.row_agents[i].utility += self.row_matrix[self.row_agents[i].strategy][self.col_agents[i].strategy]
            self.col_agents[i].utility += self.col_matrix[self.row_agents[i].strategy][self.col_agents[i].strategy]

    def reproduce(self):
        d = 0
        while d < self.number_of_deaths_per_generation:
            # kill lowest fitness row agent:
            kill_one_agent_with_given_utility(self.row_agents, min([e.utility for e in self.row_agents]))
            # reproduce highest fitness row agent:
            reproduce_one_agent_with_given_utility(self.row_agents, max([e.utility for e in self.row_agents]), self.mutation_rate, self.row_strategies)
            # kill lowest fitness col agent:
            kill_one_agent_with_given_utility(self.col_agents, min([e.utility for e in self.col_agents]))
            # reproduce highest fitness col agent:
            reproduce_one_agent_with_given_utility(self.col_agents, max([e.utility for e in self.col_agents]), self.mutation_rate, self.col_strategies)
            d += 1

    def simulate(self, plot=False):
        self.row_history = [[] for e in range(len(self.row_strategies))]
        self.col_history = [[] for e in range(len(self.col_strategies))]
        for g in range(self.generations):
            print "generation: %s of %s" % (g + 1, self.generations)
            for r in range(self.rounds_per_generation):
                print "\tround: %s of %s" % (r + 1, self.rounds_per_generation)
                # Reset all utilities
                for k in range(self.number_of_agents):
                    self.row_agents[k].utility = 0
                    self.col_agents[k].utility = 0
                self.play_tournament()
            self.row_distribution = return_current_strategy_distribution(self.row_agents, self.row_strategies)
            for k in range(len(self.row_strategies)):
                self.row_history[k].append(self.row_distribution[k])
            self.col_distribution = return_current_strategy_distribution(self.col_agents, self.col_strategies)
            for k in range(len(self.col_strategies)):
                self.col_history[k].append(self.col_distribution[k])

            self.reproduce()

            if plot:
                print self.row_distribution
                print self.col_distribution

#        self.row_distribution = return_current_strategy_distribution(self.row_agents, self.row_strategies)
#        self.col_distribution = return_current_strategy_distribution(self.col_agents, self.col_strategies)


#test = ABM(100, 10, 10, .3, .05, [[4, 0], [5, 2]], [[4, 5], [0, 2]])
## test = ABM(10000, 1000, 10, .0001, .02, [[1, -1], [-1, 1]], [[-1, 1], [1, -1]])
#test.simulate(True)

import matplotlib.pyplot as plt

data=[[.25],[.75]]
plt.ion()
for e in data:
    plt.plot(e, color='.3')
plt.draw()
for k in range(2):
    data[k].append([.4,.6][k])
raw_input()
for e in data:
    plt.plot(e, color='.3')
plt.draw()
for k in range(2):
    data[k].append([.5,.5][k])
raw_input()
for e in data:
    plt.plot(e)
plt.draw()
plt.show(block=True)
