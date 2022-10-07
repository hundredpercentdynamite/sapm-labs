import csv
from io import StringIO


def csvToArray(datafile):
    result = []
    reader = csv.reader(datafile, delimiter=",")
    for row in reader:
        result.append(row)
    return result


def readCsvString(string_data):
    string_stream = StringIO(string_data)
    return csvToArray(string_stream)


def task(csv_string):
    graph = readCsvString(csv_string)

    r1_nodes = {}
    r2_nodes = {}
    r5_nodes = {}

    for [r1, r2] in graph:
        r1_nodes[r1] = r1
        r2_nodes[r2] = True

    r3_nodes = {}
    r4_nodes = {}

    for [l, r] in graph:
        for [i, j] in graph:
            if r == i:
                r3_nodes[l] = True
                r4_nodes[j] = True
            if (l == i) & (r != j):
                r5_nodes[r] = True

    list1 = list(r1_nodes.keys())
    list2 = list(r2_nodes.keys())
    list3 = list(r3_nodes.keys())
    list4 = list(r4_nodes.keys())
    list5 = list(r5_nodes.keys())

    print("r1 nodes", list1)
    print("r2 nodes", list2)
    print("r3 nodes", list3)
    print("r4 nodes", list4)
    print("r5 nodes", list5)
    return [list1, list2, list3, list4, list5]


# Вызов задания
print(task("1,2\n1,3\n2,4"))
