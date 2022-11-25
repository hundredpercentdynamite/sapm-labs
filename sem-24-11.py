# A B C
table = [
    [1.5, 1, 1], # O1
    [1.5, 2.5, 3], # O2
    [3, 2.5, 2] # O3
]

tables = []
# Наполняем шаблонами
for i in range(len(table[0])):
    tables.append([
        [0.5, 0, 0],
        [0, 0.5, 0],
        [0, 0, 0.5],
    ])
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
        rowValue = table[iRow][iTable]
        for iCell in range(len(tables[iTable][iRow])):
            currTableValue = table[iCell][iTable]
            if currTableValue < rowValue:
                tables[iTable][iRow][iCell] = 1
            if currTableValue > rowValue:
                tables[iTable][iRow][iCell] = 0
            if currTableValue == rowValue:
                tables[iTable][iRow][iCell] = 0.5


