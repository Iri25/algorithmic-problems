def worsOnlyOnce(words):
    '''
     determines words that appear only once
    :param words: a list
    :return: a list
    '''

    if words == "":
        return []
    wordList = words.split(" ")
    tempList = {}
    aux = {}
    result = []
    for i in range(len(wordList)):
        if wordList[i] in tempList:
            aux[wordList[i]] = 0
            tempList[wordList[i]] = 0
        else:
            tempList[wordList[i]] = 1

    for j in tempList:
        if j not in aux:
            result.append(j)
    return result


assert worsOnlyOnce("") == []
assert worsOnlyOnce("deea dela deea") == ['dela']
assert worsOnlyOnce("dalia") == ['dalia']

if __name__ == '__main__':
    words = "ana are ana are mere rosii ana"
    print(worsOnlyOnce(words))

