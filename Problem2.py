import math

def distance(x, y):
    '''
    determines the distance Euclid
    :param x: a tuple
    :param y: a tuple
    :return: a float
    '''

    i = (x[1] - x[0]).__pow__(2)
    j = (y[1] - y[0]).__pow__(2)
    result = i + j
    return math.sqrt(result)


assert distance((-2, 0), (0, 0)) == 2.0
assert distance((0, 0), (0, 0)) == 0.0
assert distance((1, 9), (1, 7)) == 10.0


if __name__ == '__main__':
    x = (1, 5)
    y = (4, 1)
    print(distance(x, y))