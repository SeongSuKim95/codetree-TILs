import sys
from collections import deque


# sys.stdin = open('../../TestCode/input.txt', 'r')

N, M, K = list(map(int,sys.stdin.readline().split()))

# 0 : 빈칸
# 1 : 머리
# 2 : 몸
# 3 : 꼬리
# 4 : 이동 선
grid = [
    list(map(int,sys.stdin.readline().split()))
    for _ in range(N)
]
dirs = [(0,1),(-1,0),(0,-1),(1,0)]
def getStartPoints():

    startPoints = []
    # 0: 우, 1: 상, 2: 좌, 3: 하
    for i in range(N):
        startPoints.append((i,0,0))
    for i in range(N):
        startPoints.append((N-1,i,1))
    for i in range(N-1,-1,-1):
        startPoints.append((i,N-1,2))
    for i in range(N-1,-1,-1):
        startPoints.append((i,N-1,3))

    return startPoints

def printArr(arr):
    print()

    for row in arr:
        print(*row)

def inRange(x,y):

    return 0<=x<N and 0<=y<N

HEAD = 1
BODY = 2
TAIL = 3
PATH = 4
EMPTY = 0
BODIES = [BODY, TAIL, HEAD]
SCORE = 0
startPoints = getStartPoints()
def findHead():
    curHeads = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == HEAD:
                curHeads.append((i,j))
    return curHeads
# 1 : 2 가 꼬리 방향, 그외 0이 아닌 숫자가 있는 방향이 머리 방향
# 2 : 방문하지 않은 좌표가 있는 방향이 꼬리 방향, 방문한 좌표가 있는 방향이 머리 방향
# 3 : 2가 있는 방향이 머리 방향, 꼬리의 끝
def findTeam(hx,hy):

    visited = [
        [0] * N
        for _ in range(N)
    ]
    dxs,dys = [-1,0,1,0],[0,1,0,-1]
    nhx,nhy = -1,-1
    nbx,nby = -1,-1
    for dx,dy in zip(dxs,dys):
        nx,ny = hx+dx,hy+dy
        if inRange(nx,ny) and (grid[nx][ny] == TAIL or grid[nx][ny] == PATH):
            nhx,nhy = nx,ny
        if inRange(nx,ny) and grid[nx][ny] == BODY:
            nbx,nby = nx,ny

    curTeam = [(nhx,nhy),(hx,hy),(nbx,nby)]
    visited[hx][hy] = 1
    q = deque([(nbx,nby)])
    visited[nbx][nby] = 1
    while q:
        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cx+dx, cy+dy
            if inRange(nx,ny) and not visited[nx][ny] and (grid[nx][ny] in BODIES):
                curTeam.append((nx,ny))
                q.append((nx,ny))
                visited[nx][ny] = 1

    return curTeam

def moveTeam(teamList):

    nextGrid = [
        [0] * N
        for _ in range(N)
    ]

    for i in range(N):
        for j in range(N):
            if grid[i][j] != EMPTY:
                nextGrid[i][j] = PATH

    for members in teamList:
        nhx,nhy = members[0]
        nextGrid[nhx][nhy] = HEAD

        for bx,by in members[1:-2]:
            nextGrid[bx][by] = BODY

        tx,ty = members[-2]
        nextGrid[tx][ty] = TAIL

    for i in range(N):
        for j in range(N):
            grid[i][j] = nextGrid[i][j]

def changeDir(bx,by):
    global SCORE
    visited = [
        [0] * N
        for _ in range(N)
    ]

    dist = [
        [1] * N
        for _ in range(N)
    ]
    dxs,dys = [-1,0,1,0],[0,1,0,-1]

    q = deque([(bx,by)])
    visited[bx][by] = 1
    TAILFLAG, HEADFLAG = False, False
    tail, head = (-1,-1), (-1,-1)

    # 공을 잡은 사람이 꼬리거나, 머리일 경우
    if grid[bx][by] == TAIL:
        TAILFLAG = True
        tail = (bx, by)

    if grid[bx][by] == HEAD:
        HEADFLAG = True
        head = (bx, by)
        # print(dist[bx][by]**2)
        SCORE += dist[bx][by] ** 2

    # 몸통 탐색
    while q and not (TAILFLAG and HEADFLAG):
        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cx + dx, cy + dy
            if inRange(nx,ny) and not visited[nx][ny] and (grid[nx][ny] in BODIES):
                if grid[nx][ny] == TAIL :
                    TAILFLAG = True
                    tail = (nx,ny)
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[cx][cy] + 1
                elif grid[nx][ny] == HEAD :
                    HEADFLAG = True
                    head = (nx,ny)
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[cx][cy] + 1
                    SCORE += dist[nx][ny] ** 2
                else :
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[cx][cy] + 1
    # print(tail,head)
    grid[head[0]][head[1]], grid[tail[0]][tail[1]] = TAIL, HEAD

def throwBall(ballInfo):

    ball_x, ball_y, ball_d = ballInfo
    dx,dy = dirs[ball_d]

    while True:
        if not inRange(ball_x,ball_y):
            break
        if grid[ball_x][ball_y] in BODIES:
            changeDir(ball_x,ball_y) # score 반영도 여기서 함께 해줌
            break
        ball_x, ball_y = ball_x + dx, ball_y + dy

# printArr(grid)
for round in range(K):

    curHeads = findHead()
    ballInfo = startPoints[round % (4*N)]

    teamList = []
    for hx,hy in curHeads:
        members = findTeam(hx,hy)
        teamList.append(members[:])

    moveTeam(teamList) # grid update
    # printArr(grid)
    throwBall(ballInfo)

print(SCORE)