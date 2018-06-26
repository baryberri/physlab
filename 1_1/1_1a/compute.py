def compute(table):
    """
    Compute function for lab 1-1a. Newton's Apple
    """

    num_data = len(table)
    temp_table = [[0 for _ in range(2)] for _ in range(num_data - 1)]

    for i in range(num_data - 1):
        dt = table[i + 1][0] - table[i][0]
        dy = (table[i][2] - table[i + 1][2]) * 0.01
        temp_table[i][0] = (table[i + 1][0] + table[i][0]) / 2
        temp_table[i][1] = dy / dt

    g = [0 for _ in range(num_data - 2)]
    for i in range(num_data - 2):
        dt = temp_table[i + 1][0] - temp_table[i][0]
        dv = temp_table[i + 1][1] - temp_table[i][1]
        g[i] = dv / dt

    return g
