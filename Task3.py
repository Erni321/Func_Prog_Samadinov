def getRow(rowIndex: int):
    row = [1] * (rowIndex + 1)

    for i in range(1, rowIndex):
        for j in range(i, 0, -1):
            row[j] = row[j] + row[j - 1]

    return row
print(getRow(4)) # 1, 4, 6, 4, 1