import sys

# sys.stdin = open('input.txt','r')

attacks = []
# N : 격자 크기, M : 라운드 수
N, M = list(map(int,sys.stdin.readline().split()))

grid = [
    list(map(int,sys.stdin.readline().split()))
    for _ in range(N)
]

score = 0
# 0 1 2 3
# 우 하 좌 상
dirs = [
    (0,1),
    (1,0),
    (0,-1),
    (-1,0)
]
for _ in range(M):
    # d, p 방향, 칸수
    attacks.append(tuple(map(int,sys.stdin.readline().split())))

def createNewNums(numList):
    curNum,cnt,nIdx = -1,0,0
    newNumList = [0] * len(numList)
    for idx,num in enumerate(numList):
        if idx == 0 :
            curNum,cnt = num,1
            continue
        if num : # 0 인 경우 제외
            if curNum == num :
                cnt += 1
            else :
                newNumList[nIdx] = cnt
                nIdx += 1
                if nIdx >= len(numList):
                    return newNumList
                newNumList[nIdx] = curNum
                nIdx += 1
                if nIdx >= len(numList):
                    return newNumList
                curNum = num
                cnt = 1

    newNumList[nIdx] = cnt
    nIdx += 1
    if nIdx >= len(numList):
        return newNumList
    newNumList[nIdx] = curNum

    return newNumList
def explodeSameNums(numList):
    global score
    curNumList = numList[:][1:]
    while True :
        isExploded = False
         # 시작점 제외
        nextNumList, nIdx = [0] * len(curNumList), 0
        curNum,cnt,cIdx = -1,0,0
        for idx,num in enumerate(curNumList):
            if idx == 0 :
                curNum = num
                cnt += 1
                continue
            if num : # 0이 아니면
                if curNum == num :
                    cnt += 1
                    cIdx = idx
                else :
                    # cnt < 4 인 경우
                    # - 지금까지의 숫자들을 nextNumList에 적어주고 curNum = num ,cnt = 1로 초기화
                    #    cnt= 3인 경우  1  2  3  idx
                    if cnt < 4:
                        for i in range(cnt-1,-1,-1):
                            nextNumList[nIdx] = curNumList[cIdx - i]
                            nIdx += 1
                    else: # cnt >= 4 인 경우 폭발, curNum = num ,cnt = 1로 초기화
                        isExploded = True
                        score += curNum * cnt
                    # 초기화
                    curNum = num
                    cnt = 1
                    cIdx = idx
        if cnt < 4 :
            for k in range(cnt-1,-1,-1):
                nextNumList[nIdx] = curNumList[cIdx-k]
                nIdx += 1
        else :
            isExploded = True
            score += curNum * cnt
        if not isExploded :
            # 마지막에 센 숫자들 넣어줘야함
            return nextNumList
        curNumList = nextNumList[:]

def fillEmptySpace(curNumList):

    curNums = curNumList[1:] # 시작점 제외
    nextNums = [0] * len(curNums)

    # 비어있는 칸 땡겨주기
    nIdx = 0
    for num in curNums :
        if num:
            nextNums[nIdx] = num
            nIdx += 1

    return [0] + nextNums

def attack(cd,cp):
    global score
    cx, cy = N//2, N//2
    dx, dy = dirs[cd]

    for _ in range(cp):
        cx, cy = cx + dx, cy + dy
        score += grid[cx][cy]
        grid[cx][cy] = 0

def getCurveNums():
    cx,cy,cd = N//2, N//2, 3 # 왼쪽 방향 + 1
    numList = [grid[cx][cy]]
    # N - 1까지 두번씩 , + N-1 만큼 한번 더 추가 해야함
    for length in range(1,N):

        for i in range(2):
            cd = (cd - 1 + 4) % 4 # 방향 바꾸기
            for j in range(length):
                cx,cy = cx + dirs[cd][0], cy + dirs[cd][1]
                numList.append(grid[cx][cy])

    for _ in range(N-1):
        cx, cy = cx + dirs[cd][0], cy + dirs[cd][1]
        numList.append(grid[cx][cy])

    return numList

def moveToGrid(newNumList):

    cx,cy,cd,nIdx = N//2, N//2, 3, 0 # 왼쪽 방향 + 1
    grid[cx][cy] = 0
    # N - 1까지 두번씩 , + N-1 만큼 한번 더 추가 해야함
    for length in range(1,N):

        for i in range(2):
            cd = (cd - 1 + 4) % 4 # 방향 바꾸기
            for j in range(length):
                cx,cy = cx + dirs[cd][0], cy + dirs[cd][1]
                grid[cx][cy] = newNumList[nIdx]
                nIdx += 1

    for _ in range(N-1):
        cx, cy = cx + dirs[cd][0], cy + dirs[cd][1]
        grid[cx][cy] = newNumList[nIdx]
        nIdx += 1

for cd,cp in attacks:
    attack(cd,cp)
    numList = getCurveNums()
    newNumList = fillEmptySpace(numList)
    nextNumList = explodeSameNums(newNumList)
    finalNumList = createNewNums(nextNumList)
    moveToGrid(finalNumList)
print(score)