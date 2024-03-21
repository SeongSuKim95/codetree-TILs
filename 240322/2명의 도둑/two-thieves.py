N,M,C = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(N)]

# 연속된 M개의 열을 훔침
# 무게의 합이 C를 넘지 말아야함

# (i,j) --> j + M <= N
# 만약에 i가 같으면?
# (i,j1), (i,j2)
# j1 ~ j1 + M - 1
# j2 ~ j2 + M - 1 

# 중복 되지 않는 조건
# j1 > j2 + M - 1  and j2 < j1 + M - 1
# j2 > j1 + M - 1  and j1 < j2 + M - 1

answer = 0
selectedPos = [];
selectedWeight = [];
maximumValue = 0
def isDuplicate(pos1,pos2):
    i1,j1 = pos1
    i2,j2 = pos2
    if i1 != i2:
        return False
    else :
        if (j1 > j2 + M - 1  and j2 < j1 + M - 1) or (j2 > j1 + M - 1  and j1 < j2 + M - 1):
            return False
        else :
            return True

def getMaximumWeight(pos,colIdx,weightSum):
    global maximumValue
    
    if weightSum <= C and colIdx <= pos[1] + M -1:
        value = 0
        for Idx in selectedWeight:
            value += grid[pos[0]][Idx] ** 2
        maximumValue = max(value,maximumValue)
    else :
        return
    for i in range(N):
        selectedWeight.append(i+colIdx)
        getMaximumWeight(pos,i+colIdx + 1,weightSum + grid[pos[0]][colIdx])
        selectedWeight.pop()

def selectPos(idx):
    global answer
    global maximumValue
    if idx == 2 :
        pos1,pos2 = selectedPos[0], selectedPos[1]
        if isDuplicate(pos1,pos2):
            return
        maximumValue = 0
        getMaximumWeight(pos1,0,0)
        max1 = maximumValue
        maximumValue = 0
        getMaximumWeight(pos2,0,0)
        max2 = maximumValue
        answer = max(answer,max1+max2)
        return 

    for i in range(N):
        for j in range(N):
            if j + M <= N:
                selectedPos.append((i,j))
                selectPos(idx+1)
                selectedPos.pop()

selectPos(0)
print(answer)