import Abm
number_of_agents = 1000
generations = 100
rounds_per_generation = 5
death_rate = .1
mutation_rate = .2
row_matrix = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
col_matrix = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]

g = Abm.ABM(number_of_agents, generations, rounds_per_generation, death_rate, mutation_rate, row_matrix, col_matrix)

g.simulate(plot=True)
