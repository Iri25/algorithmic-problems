import random

def frequency1(matrix):
    '''
    determines the index of the line that most often contains 1
    :param matrix: a matrix
    :return: integer
    '''

    global result
    if matrix == [[]]:
        return [[]]
    index = 0
    maxim = -1
    freq = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for line in matrix:
        for k in range(len(line)):
            freq[index][line[k]] = freq[index][line[k]] + 1
        if freq[index][1] > maxim:
            maxim = freq[index][1]
            result = index
        index = index + 1
    return result


assert frequency1([[]]) == [[]]
assert frequency1([[0, 1, 1], [1, 1, 1]]) == 1
assert frequency1([[0, 1, 1], [1, 1, 1]]) == 1


if __name__ == '__main__':
    n = 3; m = 4
    i = 1; j = 1
    numbers = []; matrix = []
    while i <= n:
        j = 1
        while j <= m:
            numbers.append(random.randint(0, 1))
            j = j + 1
        i = i + 1
        numbers.sort()
        matrix.append(numbers)
        numbers = []

    print(matrix)
    print(frequency1(matrix))


