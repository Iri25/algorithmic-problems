def kmax(numbers, k):
    '''
    determines the kth largest element of list
    :param numbers: a list
    :param k: an integer
    :return: integer
    '''

    if not numbers:
        return []
    end = len(numbers)
    if k >= end:
        return False
    sorted = False
    while not sorted:
        sorted = True
        for i in range(end - 1):
            if numbers[i + 1] > numbers[i]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                sorted = False

    return numbers[k-1]


assert kmax([], 1) == []
assert kmax([], 5) == []
assert kmax([2, 7, 5], 1) == 7
assert kmax([2, 7, 5], 8) == False
assert kmax([9, 6, 2, 7, 5], 3) == 6
assert kmax([2, 1, 3, 8, 6, 5, 4], 6) == 2

if __name__ == '__main__':
    numbers = [7, 4, 6, 3, 9, 1]
    k = 2
    print(kmax(numbers, k))