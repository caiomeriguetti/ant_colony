import random


class PathData(object):

    def __init__(self, n):

        self.feromon = create_matrix(n, fixed_value = 1)
        self.costs = create_matrix(n, random_values = True)


def create_matrix(n, random_values = False, random_factor = 100, fixed_value = None):
    lines = []
    for i in range(0, n):
        line = []
        for j in range(0, n):

            if fixed_value:
                line.append(fixed_value)
            else:
                if random_values:
                    line.append(int(random.random() * random_factor))
                else:
                    line.append(None)
        lines.append(line)

    return lines
