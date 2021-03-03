def lastWord(words):
    '''
    determines the last alphabetical word
    :param words: a list
    :return: a char
    '''

    if words == "":
        return []
    wordList = words.split(" ")
    end = len(wordList)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(end - 1):
            if wordList[i+1] < wordList[i]:
                wordList[i], wordList[i+1] = wordList[i+1], wordList[i]
                sorted = False
    return wordList[end-1]


assert lastWord("") == []
assert lastWord("tralala") == "tralala"
assert lastWord("alabala portocala si alabala ciocolata") == "si"


if __name__ == '__main__':
    words = "Ana are mere rosii si galbene"
    print(lastWord(words))