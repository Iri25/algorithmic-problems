def frequency(numbers):
    '''
    determines the element with frequency greater than or equal to n / 2
    :param numbers: a list
    :return: integer
    '''

    if not numbers:
        return []
    k = len(numbers) // 2
    maxim = - 1
    freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(numbers)):
            freq[numbers[i]] = freq[numbers[i]] + 1
            if maxim < freq[numbers[i]] and freq[numbers[i]] >= 1:
                maxim = numbers[i]

    if max(freq) > k:
        return maxim
    else:
        return False


assert frequency([]) == []
assert frequency([2, 8, 8, 2, 8, 5, 8]) == 8
assert frequency([9, 7, 3, 9, 2, 5, 2]) == False
assert frequency([3, 7, 2, 9, 6, 5, 1]) == False

if __name__ == '__main__':
    numbers = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
    print(frequency(numbers))