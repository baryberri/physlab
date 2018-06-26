import math


def compute_x_velocity(table):
    """
    Compute x-axis velocity, assuming it is always constant.
    """
    index = len(table) - 1

    dt = table[index][0] - table[0][0]
    dx = (table[0][1] - table[index][1]) * 0.01

    return dx / dt


def compute_initial_velocity(x_velocity, degree):
    """
    Compute v0, with given x_velocity and degree.
    """
    return x_velocity / math.cos(degree * math.pi / 180)


def compute_y_at_times(initial_velocity, degree, times_to_compute):
    """
    Return y(t) for given t.
    """
    y = []
    term_1 = initial_velocity * math.sin(degree * math.pi / 180)
    term_2 = 9.80665 / 2
    for t in times_to_compute:
        y.append(term_1 * t - term_2 * t * t)
    return y


def get_ys(table):
    """
    get dy.
    """
    initial_y = table[0][2]
    ys = []
    for i in range(len(table)):
        ys.append((table[i][2] - initial_y) * 0.01)
    return ys


def get_times(table):
    """
    extract time to compute.
    """
    time = []
    for i in range(len(table)):
        time.append(table[i][0])
    return time


def rms(ys, theory_ys):
    """
    Compute rms.
    """
    result = 0
    for i in range(len(ys)):
        result += ((ys[i] - theory_ys[i]) ** 2)
    result /= len(ys)
    return math.sqrt(result)