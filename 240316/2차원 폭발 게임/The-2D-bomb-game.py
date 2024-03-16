N,M,K = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(N)]

# 행 방향으로 M개 이상 터뜨리기

def explode():
    global grid    
    explodeFlag = False
    for col in range(N):
        curArr = [grid[i][col] for i in range(N)] + [0]
        curCnt = 1
        for Idx in range(N):
            if curArr[Idx] and curArr[Idx] == curArr[Idx+1]:
                curCnt += 1
            else : 
                if curCnt >= M :
                    for i in range(Idx,Idx-curCnt,-1):
                        curArr[i] = 0
                    explodeFlag = True
                curCnt = 1 # 초기화

        for row in range(N):
            grid[row][col] = curArr[row]

    return explodeFlag # False 일 경우 더이상 폭발 진행 안된 것

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
    Flag = True
    while Flag :  
        Flag = explode()
        gravity()
    # 2. 회전
    rotateClock()
# K번 회전 후
Flag = True
while Flag:
    Flag = explode()
    gravity()

print(countNonzero())