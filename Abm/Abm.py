from __future__ import division
import copy
import random


class Agent():
    """
    An agent class
    """
    def __init__(self, strategy):
        self.strategy = strategy
        self.utility = 0


def kill_one_agent_with_given_utility(agents, utility):
    """
    This method is used to delete a particular agent with given utility
    """
    number_of_agents = len(agents)
    k = 0
    while len(agents) == number_of_agents:
        if agents[k].utility == utility:
            del agents[k]
        k += 1


def reproduce_one_agent_with_given_utility(agents, utility, mutation_rate, strategies):
    """
    Deep copy an agent with a given utility. When copying an agent there is a potential mutation that will make the new agent have a different strategy.
    """
    number_of_agents = len(agents)
    k = 0
    while len(agents) == number_of_agents:
        if agents[k].utility == utility:
            agents.append(copy.deepcopy(agents[k]))
            if random.random() < mutation_rate:
                agents[-1].strategy = random.choice([s for s in strategies if s != agents[-1].strategy])
        k += 1


def return_current_strategy_distribution(agents, strategies):
    """
    This function returns the current strategy distribution amongst a set of agents.
    """
    frequencies = []
    for s in strategies:
        frequencies.append(0)
        for e in agents:
            if e.strategy == s:
                frequencies[-1] += 1
    return [e / len(agents) for e in frequencies]


class ABM():
    """
    This is a class defining an ABM of a game.
    """
    def __init__(self, number_of_agents, generations, rounds_per_generation, death_rate, mutation_rate, row_matrix, col_matrix, initial_strategy_distribution=False):
        """
        Initialize all variables
        """
        self.number_of_agents = number_of_agents
        self.generations = generations
        self.rounds_per_generation = rounds_per_generation
        self.death_rate = death_rate
        self.number_of_deaths_per_generation = int(number_of_agents * death_rate)
        self.mutation_rate = mutation_rate
        self.row_strategies = range(len(row_matrix))
        self.col_strategies = range(len(col_matrix[0]))
        self.row_matrix = row_matrix
        self.col_matrix = col_matrix
        if not initial_strategy_distribution:
            # If no initial strategy distribution is passed
            self.row_agents = [Agent(random.choice(self.row_strategies)) for e in range(number_of_agents)]
            self.col_agents = [Agent(random.choice(self.col_strategies)) for e in range(number_of_agents)]
        else:
            # Include code to pick agents according to a given distribution
            self.row_agents = [Agent(random.choice([strategy for strategy in initial_strategy_distribution[0] for count in range(initial_strategy_distribution[0][strategy])])) for e in range(number_of_agents)]
            self.col_agents = [Agent(random.choice([strategy for strategy in initial_strategy_distribution[1] for count in range(initial_strategy_distribution[1][strategy])])) for e in range(number_of_agents)]

    def play_tournament(self):
        """
        This randomly plays all row agents against all column agents.
        """
        # Here we shuffle all column players
        random.shuffle(self.col_agents)
        for i in range(self.number_of_agents):
            # Increment utilities of each player
            self.row_agents[i].utility += self.row_matrix[self.row_agents[i].strategy][self.col_agents[i].strategy]
            self.col_agents[i].utility += self.col_matrix[self.row_agents[i].strategy][self.col_agents[i].strategy]

    def reproduce(self):
        """
        This kills enough row and col players with lowest utility so as to fit with death rate. After that we reproduce players with highest utility to ensure we have constant population numbers.
        """
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
        """
        This runs the simulation.
        """
        # Initialising history lists for distribution of strategies

        # Some debugging
        # import pdb
        # pdb.set_trace()

        self.row_history = [[] for e in range(len(self.row_strategies))]
        self.col_history = [[] for e in range(len(self.col_strategies))]
        if plot:
            # If plot is true we plot the strategy distributions dynamically
            import matplotlib.pyplot as plt
            import matplotlib.cm as cm
            plt.ion()  # Turn interactive mode on (so that we can graph dynamically.
            plt.ylim(0, 1)  # Set ylim to have min 0 and max 1
            plt.xlabel("Generations (max=%s)" % self.generations)  # Label for x axis
            plt.ylabel("Probability")  # Label for y axis
            for k in range(len(self.row_strategies)):
                # Plot all row strategies
                c = cm.spring((k + 1) / len(self.row_strategies))
                plt.plot(self.row_history[k], color=c, label="Row strategy: %s" % (k + 1))
            for k in range(len(self.col_strategies)):
                # Plot all col strategies
                c = cm.winter((k + 1) / len(self.col_strategies))
                plt.plot(self.col_history[k], "--", color=c, label="Col strategy: %s" % (k + 1))

            plt.legend(loc="upper left")
            plt.draw()

        for g in range(self.generations):
            # In a loop for every generation
            print "\n----------------------"
            print "\nGeneration: %s of %s" % (g + 1, self.generations)
            for r in range(self.rounds_per_generation):
                # Loop to repeat tournament for each generation
                print "\tRound: %s of %s" % (r + 1, self.rounds_per_generation)
                # Reset all utilities before starting a tournament
                for k in range(self.number_of_agents):
                    self.row_agents[k].utility = 0
                    self.col_agents[k].utility = 0
                self.play_tournament()
            # Calculate distributions and update history
            self.row_distribution = return_current_strategy_distribution(self.row_agents, self.row_strategies)
            for k in range(len(self.row_strategies)):
                self.row_history[k].append(self.row_distribution[k])
            self.col_distribution = return_current_strategy_distribution(self.col_agents, self.col_strategies)
            for k in range(len(self.col_strategies)):
                self.col_history[k].append(self.col_distribution[k])
            print "\nRow players strategy distribution:"
            print "\t", self.row_distribution
            print "\nCol players strategy distribution:"
            print "\t", self.col_distribution
            # Reproduce
            self.reproduce()

            if plot:
                # Update the plot if plot is True
                for k in range(len(self.row_strategies)):
                    c = cm.spring((k + 1) / len(self.row_strategies))
                    plt.plot(self.row_history[k], color=c)
                for k in range(len(self.col_strategies)):
                    c = cm.winter((k + 1) / len(self.col_strategies))
                    plt.plot(self.col_history[k], "--", color=c)
                plt.draw()
        if plot:
            # Block plot at end of simulation
            plt.show(block=True)
