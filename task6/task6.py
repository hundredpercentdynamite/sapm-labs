import json

import numpy as np

def getComparisons(ranks):
    tables = []
    # Наполняем шаблонами
    n = len(ranks)
    m = len(ranks[0])
    for i in range(m):
        template = np.zeros((n, n))
        np.fill_diagonal(template, 0.5)
        tables.append(template)
    # Для самопроверки
    # tableA = [
    #     [0.5, 0.5, 0],
    #     [0.5, 0.5, 0],
    #     [1, 1, 0.5],
    # ]
    #
    # tableB = [
    #     [0.5, 0, 0],
    #     [1, 0.5, 0.5],
    #     [1, 0.5, 0.5],
    # ]
    #
    # tableC = [
    #     [0.5, 0, 0],
    #     [1, 0.5, 1],
    #     [1, 0, 0.5],
    # ]

    # Перебираем шаблоны и сравниваем табличные значения
    for iTable in range(len(tables)):
        for iRow in range(len(tables[iTable])):
            rowValue = ranks[iRow][iTable]
            for iCell in range(len(tables[iTable][iRow])):
                currTableValue = ranks[iCell][iTable]
                if currTableValue > rowValue:
                    tables[iTable][iRow][iCell] = 1
                if currTableValue < rowValue:
                    tables[iTable][iRow][iCell] = 0
                if currTableValue == rowValue:
                    tables[iTable][iRow][iCell] = 0.5
    return tables

def calcX(compares):
    rowsCount = len(compares[0])
    cellsCount = len(compares[0][0])
    expCount = len(compares)
    result = np.zeros((rowsCount, cellsCount))
    for i in range(0, rowsCount):
        for j in range(0, cellsCount):
            mi = 0
            mp = 0
            mj = 0
            for t in range(0, expCount):
                value = compares[t][i][j]
                if value == 1:
                    mi += 1
                elif value == 0.5:
                    mp += 1
                else:
                    mj += 1
            resIJ = (1 * (mi / expCount)) + (0.5 * (mp / expCount)) + (0 * (mj / expCount))
            result[i][j] = resIJ
    return result

#     # вариант из тетради
# def calcGeneralEstimation(xTable, E):
#     n = len(xTable[0])
#     kPrev = np.ones(n) / n
#     kNew = None
#     while True:
#         y = np.matmul(xTable, kPrev)
#         a = np.matmul(xTable, np.ones(n).transpose())
#         lbd = np.matmul(a, y)
#         kNew = (1 / lbd) * np.matmul(np.asarray(xTable).transpose(), y)
#         diff = abs(kNew - kPrev)
#         max = diff.max()
#         if max <= E:
#             break
#         else:
#             kPrev = kNew
#     return kNew


def calcGeneralEstimation(xTable, E):
    n = len(xTable[0])
    kPrev = np.ones(n) / n
    kNew = None
    while True:
        y = np.matmul(xTable, kPrev)
        lbd = np.matmul(np.ones(n), y)
        kNew = (1 / lbd) * y
        diff = abs(kNew - kPrev)
        max = diff.max()
        if max <= E:
            break
        else:
            kPrev = kNew
    return np.around(kNew, 3)

def parseJsonString(str):
    return json.loads(str)

def task(jsonString):
    table = np.array(parseJsonString(jsonString)).transpose()

    comparisons = getComparisons(table)
    X = calcX(comparisons)
    K = calcGeneralEstimation(X, 0.001)
    result = json.dumps(K.tolist())
    return result
