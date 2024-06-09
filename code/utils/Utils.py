def sortDictionaryByValue(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)


def sortDictionaryByKey(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[0], reverse=False)


def printKill(message):
    print(message)
    exit(1)
