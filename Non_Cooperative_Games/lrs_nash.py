"""
A library to use the lrs Nash library. This is currently done in a pretty poor way.
"""
from subprocess import Popen, PIPE, call
from os import remove


def multiple_equilibria_clean(l):
    if len(l) > 2:
        r = []
        for e in l[:-1]:
            r.append([e, l[-1]])
        return r
    return [l]


class Normal_Form_Game:
    """
    A class for a normal form game
    """
    def __init__(self, row_matrix, col_matrix):
        self.row_size = len(row_matrix)
        self.col_size = len(row_matrix[0])
        self.row_matrix = row_matrix
        self.col_matrix = col_matrix

    def solve(self):
        """
        Method that write physical files so that lrs can be used to solve game.
        """
        # Write game file
        game = open("game", "w")
        game.write("%s %s\n" % (self.row_size, self.col_size))
        for i in self.row_matrix:
            game.write("\n")
            game.write(" ".join([str(e) for e in i]))
        game.write("\n")
        for j in self.col_matrix:
            game.write("\n")
            game.write(" ".join([str(e) for e in j]))
        game.close()

        # Write H representations for each player (really should automate this)
        call(["lrslib-043/setupnash", "game", "game1", "game2"], stdout=PIPE)
        # Solve game using lrs:
        process = Popen(["lrslib-043/nash", "game1", "game2"], stdout=PIPE)
        # Save output
        self.lrs_output = [row for row in process.stdout]
        # Delete lrs files
        for f in ["game", "game1", "game2"]:
            remove(f)
        # Find number of equilibria
        self.number_of_equilibria = eval([row for row in self.lrs_output if "*Number of equilibria found:" in row][0].split()[-1])
        self.lrs_output = [[eval(e) for e in row[:-2].split('  ')] for row in self.lrs_output[7:-7] if row != '\n']
        print self.lrs_output
        self.equilibria = []
        while self.lrs_output:
            if len(self.lrs_output) > 1:
                i = [row[0] for row in self.lrs_output].index(1)
                temp = []
                for e in self.lrs_output[: i + 1]:
                    temp.append(self.lrs_output.pop(0))
                self.equilibria.append(multiple_equilibria_clean(temp))


a = Normal_Form_Game([[1, 2], [3, 2]], [[0, 1], [1, 0]])
a.solve()
print a.number_of_equilibria
print a.lrs_output
print a.equilibria
