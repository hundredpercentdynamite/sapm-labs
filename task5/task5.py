import numpy as np
import collections.abc
import json

def flat(arr):
    result = []
    for elem in arr:
        if not isinstance(elem, str) and isinstance(elem, collections.abc.Sequence):
            result = result + flat(elem)
        else:
            result.append(elem)
    return result


def getRelationMatrix(arr):
    flatArr = flat(arr)
    flatArrLen = len(flatArr)
    result = np.zeros((flatArrLen, flatArrLen))
    for i in range(flatArrLen):
        value = int(flatArr[i]) - 1
        for j in range(i + 1):
            rightValue = int(flatArr[j]) - 1
            result[rightValue][value] = 1
    for group in arr:
        if not isinstance(group, str) and isinstance(group, collections.abc.Sequence):
            for k in range(len(group)):
                value = int(group[k]) - 1
                for z in range(len(group)):
                    rightValue = int(group[z]) - 1
                    result[value][rightValue] = 1
                    result[rightValue][value] = 1
    return result

def calcCore(a, b):
    transposedRelationA = np.transpose(a)
    transposedRelationB = np.transpose(b)

    relationAB = np.multiply(a, b)
    transposedRelationAB = np.multiply(transposedRelationA, transposedRelationB)
    result = np.logical_or(relationAB, transposedRelationAB)

    core = []
    for i in range(len(result)):
        for j in range(i, len(result[i])):
            if result[i][j] == False:
                core.append([str(i + 1), str(j + 1)])

    return core
def parseJsonString(str):
    return json.loads(str)


def task(strA, strB):
    A = parseJsonString(strA)
    B = parseJsonString(strB)
    relationA = getRelationMatrix(A)
    relationB = getRelationMatrix(B)

    core = calcCore(relationA, relationB)
    return core
