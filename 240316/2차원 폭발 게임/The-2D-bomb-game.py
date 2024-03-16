N,M,K = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(N)]

# 행 방향으로 M개 이상 터뜨리기

def explode():
    global grid    
    for col in range(N):
        explodeFlag = True
        curArr = [grid[i][col] for i in range(N)] + [0]
        while explodeFlag :
            explodeFlag = False
            
            curCnt = 1
            # print(curArr,col)
            for Idx in range(N):
                if curArr[Idx] and curArr[Idx] == curArr[Idx+1]:
                    curCnt += 1
                else : 
                    if curCnt >= M :
                        for i in range(Idx,Idx-curCnt,-1):
                            curArr[i] = 0
                        explodeFlag = True
                    curCnt = 1 # 초기화
            tmpArr, tmpIdx = [0] * N, N-1
            for row in range(N-1,-1,-1):
                if curArr[row]:
                    tmpArr[tmpIdx] = curArr[row]
                    tmpIdx -= 1
            for i in range(N):
                curArr[i] = tmpArr[i]
        for row in range(N):
            grid[row][col] = curArr[row]

def gravity():
    global grid
    for col in range(N):
        tmpArr, tmpIdx = [0]* N , N-1 
        for row in range(N-1,-1,-1):
            if grid[row][col]:
                tmpArr[tmpIdx] = grid[row][col]
                tmpIdx -= 1
        for row in range(N):
            grid[row][col] = tmpArr[row]
    
def rotateClock():
    global grid
    nextGrid = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            nextGrid[i][j] = grid[N-1-j][i]
    
    grid = [row[:] for row in nextGrid]

def printArr(arr):
    for row in arr:
        print(*row)
    print()

def countNonzero():
    global grid
    cnt = 0
    for row in range(N):
        for col in range(N):
            if grid[row][col]:
                cnt += 1
    return cnt

for _ in range(K):
    # 1. explosion
    explode()
    # 2. 회전
    rotateClock()
    gravity()
# K번 회전 후
explode()

print(countNonzero())