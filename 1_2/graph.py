from table_importer import TableImporter
from compute import *
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def main():
    tables = TableImporter()

    resulting_degree = None
    times = None
    table = tables.get_table()
    if table is not None:
        times = get_times(table)
        ratio = compute_ratio(table)
        atan = compute_atan(ratio)
        positive_atan = atan_to_positive(atan)
        accumulated_atan = accumulate_degree(positive_atan)
        resulting_degree = set_starting_point_to_zero(accumulated_atan)

    # do the graph
    x = []
    y = []
    l = times
    r = 2
    for i in range(len(resulting_degree)):
        x.append(r * math.cos(resulting_degree[i]))
        y.append(r * math.sin(resulting_degree[i]))
        r += 0.1

    plt.axis('auto')

    plt.figure(figsize=(11, 11))
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.plot([max(x) + 1, min(x) - 1], [0, 0], color="black")
    plt.plot([0, 0], [max(y) + 1, min(y) - 1], color="black")

    frame1 = plt.gca()
    frame1.axes.xaxis.set_ticklabels([])
    frame1.axes.yaxis.set_ticklabels([])
    plt.show()


if __name__ == '__main__':
    main()
