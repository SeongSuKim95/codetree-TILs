N, M, K, C = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

cntGrid = [
    [-1] * N
    for _ in range(N)
]
dxs,dys = [-1,1,0,0],[0,0,-1,1]

EMPTY = 0
WALL = -1
STOP = -2

answer = 0

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def grow():

    nextGrid = [
        [EMPTY] * N
        for _ in range(N)
    ]

    for i in range(N):
        for j in range(N):
            cx,cy,adjCnt = i,j,0
            if grid[cx][cy] < 0 :
                nextGrid[cx][cy] = grid[cx][cy]
            elif grid[cx][cy] == EMPTY :
                continue
            else :
                for dx,dy in zip(dxs,dys):
                    nx,ny = cx+dx, cy+dy
                    if inRange(nx,ny) and grid[nx][ny] > 0 :
                        adjCnt += 1
                nextGrid[i][j] = grid[i][j] + adjCnt

    
    for i in range(N):
        for j in range(N):
            grid[i][j] = nextGrid[i][j]

def printArr(arr):

    for row in arr:
        print(*row)
    print()


def clone():

    nextGrid = [
        [EMPTY] * N
        for _ in range(N)
    ]

    for i in range(N):
        for j in range(N):
            cx,cy = i,j
            if grid[cx][cy] < 0 :
                nextGrid[cx][cy] = grid[cx][cy]
            elif grid[cx][cy] == EMPTY :
                continue
            else :
                adjList = []
                for dx,dy in zip(dxs,dys):
                    nx,ny = cx+dx, cy+dy
                    if inRange(nx,ny) and grid[nx][ny] == EMPTY and cntGrid[nx][ny] == -1:
                        adjList.append((nx,ny))
                if len(adjList) > 0 :
                    for adjx,adjy in adjList:
                        nextGrid[adjx][adjy] += grid[cx][cy] // len(adjList)
                nextGrid[cx][cy] += grid[cx][cy]

    for i in range(N):
        for j in range(N):
            grid[i][j] = nextGrid[i][j]

def kill():
    global answer
    dxs,dys = [-1,-1,1,1],[1,-1,1,-1]
    maxKilledPos = (0,1e9,1e9)

    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0 :
                # 제초제 뿌리기
                cx,cy,killedCnt = i,j,grid[i][j]
                for dx,dy in zip(dxs,dys):
                    for r in range(1,K+1):
                        nx,ny = cx+r*dx,cy+r*dy
                        if inRange(nx,ny):
                            if grid[nx][ny] > 0 : # 나무인 경우
                                killedCnt += grid[nx][ny]
                            else :
                                break
                maxKilledPos = min((-killedCnt,cx,cy),maxKilledPos)
    killedCnt, px,py = maxKilledPos
    answer -= killedCnt
    # 이전 제초제 제거
    for i in range(N):
        for j in range(N):
            if cntGrid[i][j] > 0 :
                cntGrid[i][j] -= 1

    # 제초제 뿌리기
    grid[px][py] = STOP
    cntGrid[px][py] = C
    for dx,dy in zip(dxs,dys):
        for r in range(1,K+1):
            nx,ny = px + r*dx, py+r*dy
            if inRange(nx,ny):
                if grid[nx][ny] >= 0 :
                    grid[nx][ny] = STOP
                    cntGrid[nx][ny] = C
                else:
                    break

    for i in range(N):
        for j in range(N):
            if cntGrid[i][j] == 0 :
                grid[i][j] = EMPTY
                cntGrid[i][j] = -1

for _ in range(M):
    grow()

    clone()
  
    kill()


print(answer)