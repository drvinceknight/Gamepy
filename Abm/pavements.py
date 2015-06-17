import Abm
number_of_agents = 1000
generations = 100
rounds_per_generation = 5
death_rate = .1
mutation_rate = .2
row_matrix = [[1, -1], [-1, 1]]
col_matrix = row_matrix
initial_distribution = [{0: 50, 1: 50}, {0:50, 1:50}]

g = Abm.ABM(number_of_agents, generations, rounds_per_generation, death_rate, mutation_rate, row_matrix, col_matrix, initial_distribution)
g.simulate(plot=True)
