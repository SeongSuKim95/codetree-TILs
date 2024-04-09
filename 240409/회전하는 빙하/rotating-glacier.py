from collections import deque

N, Q = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(2**N)
]

turnLevels = list(map(int,input().split()))

def printArr(arr):

    for row in arr:
        print(*row)
    print()

def inRange(x,y):

    return 0<=x<2**N and 0<=y<2**N

def turnSmallGrid(cx,cy,level):

    scaleWhole = 2 ** level # 선택된 전체 격자
    scalePart = 2 ** (level -1)# 평행이동할 작은 격자

    curGrid = [
        [grid[i][j] for j in range(cy,cy+scaleWhole)]
        for i in range(cx,cx+scaleWhole)
    ]

    nextGrid = [
        [0] * (scaleWhole)
        for _ in range(scaleWhole)
    ] 

    movedirs = [(0,1),(1,0),(-1,0),(0,-1)]
    curdir = 0
    
    for i in range(0,scaleWhole,scalePart):
        for j in range(0,scaleWhole,scalePart):
            # 작은 격자 평행 이동
            px , py = i, j
            # print(px,py)
            for k in range(0,scalePart):
                for l in range(0,scalePart):
                    nextGrid[px+k+scalePart*movedirs[curdir][0]][py+l+scalePart*movedirs[curdir][1]] = curGrid[px+k][py+l]
            # printArr(nextGrid)
            curdir += 1
    
    for i in range(0,scaleWhole):
        for j in range(0,scaleWhole):
            grid[i+cx][j+cy] = nextGrid[i][j]

def turnGrid(level):

    scale = 2 ** level
    for sx in range(0,2**N,scale):
        for sy in range(0,2**N,scale):

            turnSmallGrid(sx,sy,level)

def meltDown():

    scale = 2**N

    nextGrid = [
        [0] * scale
        for _ in range(scale)
    ]

    dxs,dys = [-1,1,0,0],[0,0,-1,1]

    for cx in range(scale):
        for cy in range(scale):
            if grid[cx][cy] :
                adjCnt = 0
                for dx,dy in zip(dxs,dys):
                    nx,ny = cx+dx,cy+dy
                    if inRange(nx,ny) and grid[nx][ny]:
                        adjCnt += 1
                if adjCnt < 3 :
                    nextGrid[cx][cy] = grid[cx][cy] - 1
                else : 
                    nextGrid[cx][cy] = grid[cx][cy]
    
    for i in range(scale):
        for j in range(scale):
            grid[i][j] = nextGrid[i][j]
    
def countIce():
    scale = 2**N
    cnt = 0 
    for i in range(scale):
        for j in range(scale):
            cnt += grid[i][j]
    
    return cnt

def bfs():
    
    scale = 2** N
    visited = [
        [0] * scale
        for _ in range(scale)
    ]

    q = deque()

    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    maxCnt = 0

    for i in range(scale):
        for j in range(scale):
            if not visited[i][j] and grid[i][j]:
                
                q.append((i,j))
                visited[i][j] = 1
                iceCnt = 1
                
                while q: 
                    cx,cy = q.popleft()
                    for dx,dy in zip(dxs,dys):
                        nx,ny = cx+dx,cy+dy
                        if inRange(nx,ny) and not visited[nx][ny] and grid[nx][ny]:
                            q.append((nx,ny))
                            visited[nx][ny] = 1
                            iceCnt += 1

                maxCnt = max(iceCnt, maxCnt)
    return maxCnt



def simulate():

    for level in turnLevels:
        if level:
            turnGrid(level)
    meltDown()
    print(countIce())
    print(bfs())

simulate()