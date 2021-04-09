def getRow(rowIndex):
    currow = []

    currow.append(1)

    if (rowIndex == 0):
        return currow

    prev = getRow(rowIndex - 1)

    for i in range(1, len(prev)):

        curr = prev[i - 1] + prev[i]
        currow.append(curr)

    currow.append(1)

    return currow


n = 3
arr = getRow(n)

for i in range(len(arr)):

    if (i == (len(arr) - 1)):
        print(arr[i])
    else:
        print(arr[i], end=", ")