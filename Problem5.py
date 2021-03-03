def frequency2(numbers):
    '''
    determines the item that appears twice
    :param numbers: a list
    :return: integer
    '''

    if not numbers:
        return []
    maxim = - 1
    freq = [0, 0, 0, 0, 0]
    for i in range(len(numbers)):
            freq[numbers[i]] = freq[numbers[i]] + 1
            if maxim < freq[numbers[i]] == 2:
                maxim = numbers[i]
    return maxim


assert frequency2([]) == []
assert frequency2([3, 2, 3, 4, 1]) == 3
assert frequency2([2, 1, 3, 4, 1]) == 1
assert frequency2([4, 2, 3, 4, 1]) == 4

if __name__ == '__main__':
    n = 5
    numbers = [1, 2, 3, 4, 2]
    print(frequency2(numbers))