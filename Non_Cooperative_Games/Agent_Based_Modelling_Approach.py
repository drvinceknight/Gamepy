"""
Algorithm from 'Game Theory Evolving'
"""
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
    def ___init__(self, strategy):
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
            reproduce_one_agent_with_given_utility(self.row_agents, max([e.utility for e in self.row_agents]), self.row_strategies)
            # kill lowest fitness col agent:
            kill_one_agent_with_given_utility(self.col_agents, min([e.utility for e in self.col_agents]))
            # reproduce highest fitness col agent:
            reproduce_one_agent_with_given_utility(self.col_agents, max([e.utility for e in self.col_agents]), self.col_strategies)

    def simulate(self):
        for g in range(self.generations):
            for r in range(self.rounds_per_generation):
                self.play_tournament()
            self.reproduce()
