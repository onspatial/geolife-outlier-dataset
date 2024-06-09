def getAllFiles(path):
    from os import walk, path
    files = []
    for r, d, f in walk(path):
        for file in f:
            files.append(path.join(r, file))
    return files


def saveToJsonFile(data, fileName='data'):
    from json import dump
    from datetime import datetime

    now = datetime.now()
    timestamp = now.strftime("%d_%H_%M_%S")
    fileName = f'{fileName}_{timestamp}.json'

    with open(fileName, 'a') as outFile:
        dump(data, outFile)


def saveToFile(data, fileName='data'):
    from datetime import datetime

    now = datetime.now()
    timestamp = now.strftime("%d_%H")
    fileName = f'{fileName}_{timestamp}.txt'

    with open(fileName, 'a') as outFile:
        outFile.write(data)


def readPairs(fileName):
    pairs = set()
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            pair = tuple(line.strip().split(', '))
            pairs.add(pair)
    return pairs


def log(message):
    from datetime import datetime
    now = datetime.now()
    timestamp = now.strftime("%d_%H")
    fileName = f'logs/log_{timestamp}.txt'

    with open(fileName, 'a') as outFile:
        outFile.write(message + '\n')


def saveDataFrame(dataFrame, fileName):
    import config.Files as fileConfig
    dataFrame.to_csv(
        f'{fileConfig.needleRootDirectory}/{fileName}', sep=' ', index=False)
