from collections import defaultdict
r,c,k = list(map(int,input().split()))

# 행의 개수가 열의 개수보다 크거나 같은 경우
# a. 모든 행에 대하여 정렬을 수행합니다. 정렬 기준은 출현 빈도 수가 적은 순서대로 정렬을 합니다.
# b. 출현하는 횟수가 같은 숫자가 있는 경우에는 해당 숫자가 작은 순서대로 정렬을 수행합니다.
# c. 정렬을 수행할 때 숫자와 해당하는 숫자의 출현 빈도 수를 함께 출력해줍니다.

# 행의 개수가 열의 개수보다 작은 경우
# a. 모든 열에 대해 위의 과정을 수행해줍니다.
# 행이나 열의 길이가 100을 넘어가는 경우에는 처음 100개의 격자를 제외하고는 모두 버립니다.

# 목표에 도달하는 것이 불가능하거나 답이 100초 초과 시 --> -1 출력

inputGrid = [
    list(map(int,input().split()))
    for _ in range(3)
]

grid = [
    [0] * 100
    for _ in range(100)
]

for i in range(3):
    for j in range(3):
        grid[i][j] = inputGrid[i][j]

maxRow, maxCol, elapsedTime = 3, 3, 0

# 행 또는 열의 숫자 세기
def makeNewRows(rowIdx):
    global maxCol,maxRow
    numCounts = defaultdict(int)
    nextRow= [0] * 100
    curRow = grid[rowIdx]

    for curNum in curRow:
        if curNum:
            numCounts[curNum] += 1

    sortedPairs = sorted(numCounts.items(),key = lambda x : (x[1],x[0]))
    newRows = []
    for num,cnt in sortedPairs:
        newRows.append(num)
        newRows.append(cnt)

    if len(newRows) >= 100 :
        newRows = newRows[:100]

    maxCol= max(len(newRows),maxCol)

    for idx,num in enumerate(newRows):
        nextRow[idx] = num

    for j in range(maxCol):
        grid[rowIdx][j] = nextRow[j]
    
def makeNewCols(colIdx):
    global maxRow,maxCol
    numCounts = defaultdict(int)
    nextCol = [0] * 100

    curCol = []
    for i in range(100):
        curCol.append(grid[i][colIdx])

    for curNum in curCol:
        if curNum:
           numCounts[curNum] += 1

    sortedPairs = sorted(numCounts.items(),key = lambda x : (x[1],x[0]))
    newCols = []
    for num,cnt in sortedPairs:
        newCols.append(num)
        newCols.append(cnt)
    
    maxRow = max(len(newCols),maxRow)
    
    if len(newCols) >= 100 :
        newCols = newCols[:100]
    
    for idx,num in enumerate(newCols):
        nextCol[idx] = num

    for i in range(maxRow):
        grid[i][colIdx] = nextCol[i]

def printArr(arr):
    global maxRow,maxCol
    
    for i in range(maxRow):
        print(*arr[i][:maxCol])
    print()

def simulate():
    global maxRow, maxCol, elapsedTime
    while True :
        
        if grid[r-1][c-1] == k :
            break
        
        if maxRow >= maxCol :
            for rowIdx in range(maxRow):
                makeNewRows(rowIdx)
        else :
            for colIdx in range(maxCol):
                makeNewCols(colIdx)
        elapsedTime += 1

        if elapsedTime > 100 :
            elapsedTime = -1
            break
simulate()

print(elapsedTime)