import sys
from collections import deque
# sys.stdin = open('input.txt','r')
N, M = list(map(int,sys.stdin.readline().split()))
def convertStr(str):

    if str == "#":
        return WALL
    if str == ".":
        return EMPTY
    if str == "R":
        return RED
    if str == "B":
        return BLUE
    if str == "O":
        return EXIT

def printArr(arr):

    for row in arr:
        print(*row)
    print()

# 상 하 좌 우
dxs, dys = [-1,1,0,0],[0,0,-1,1]

WALL = 1
EMPTY = 0
RED = "R"
BLUE = "B"
EXIT = "X"

CANDY_OUT = (100,100)
RED_POS = (0,0)
BLUE_POS = (0,0)

grid = [
    list(map(lambda x : convertStr(x),sys.stdin.readline().rstrip('\n')))
    for _ in range(N)
]

for i in range(N):
    for j in range(M):
        if grid[i][j] == RED:
            RED_POS = (i,j)
        if grid[i][j] == BLUE :
            BLUE_POS = (i,j)

def inRange(x,y):
    return 0<=x<N and 0<=y<M
def moveOne(dir,cx,cy):
    global RED_POS, BLUE_POS
    red_pos = RED_POS
    blue_pos = BLUE_POS
    ox,oy = cx,cy
    dx,dy = dxs[dir],dys[dir]
    while True :
        nx,ny = cx+dx,cy+dy

        if grid[nx][ny] != EMPTY and grid[nx][ny] != EXIT:
            break # (cx,cy)가 바뀐 자리임!

        if grid[nx][ny] == EMPTY:
            cx,cy = nx,ny
            continue

        if grid[nx][ny] == EXIT:
            cx,cy = nx,ny
            break

    # 빨간 공인 경우
    if grid[ox][oy] == RED:
        # 기존 위치
        grid[ox][oy] = EMPTY

        # 바뀐 위치
        if grid[cx][cy] != EXIT:
            grid[cx][cy] = RED
            RED_POS = (cx,cy)
        else:
            RED_POS = CANDY_OUT

    # 빨간 공인 경우
    if grid[ox][oy] == BLUE:
        # 기존 위치
        grid[ox][oy] = EMPTY

        # 바뀐 위치
        if grid[cx][cy] != EXIT:
            grid[cx][cy] = BLUE
            BLUE_POS = (cx, cy)
        else:
            BLUE_POS = CANDY_OUT

def moveRedFirst(dir,red_pos,blue_pos):
    Rx,Ry = red_pos
    Bx,By = blue_pos
    moveOne(dir,Rx,Ry)
    moveOne(dir,Bx,By)
    return

counterDir = {
    0 : 1,
    1 : 0,
    2 : 3,
    3 : 2
}

def moveBlueFirst(dir,red_pos,blue_pos):

    Rx,Ry = red_pos
    Bx,By = blue_pos
    moveOne(dir,Bx,By)
    moveOne(dir,Rx,Ry)
    return

def checkUpward(dir):
    global RED_POS, BLUE_POS
    red_pos = RED_POS[:]
    blue_pos = BLUE_POS[:]
    if red_pos[1] == blue_pos[1] : # RED 와 BLUE가 같은 열에 있는지 확인
        if red_pos[0] < blue_pos[0]: # 행이 작은 쪽(RED) 먼저 이동
            moveRedFirst(dir,red_pos,blue_pos)
        if blue_pos[0] < red_pos[0]: # 행이 작은 쪽(BLUE) 먼저 이동
            moveBlueFirst(dir,red_pos,blue_pos)
    else:
        moveRedFirst(dir,red_pos,blue_pos)
def checkDownward(dir):
    global RED_POS, BLUE_POS
    red_pos = RED_POS[:]
    blue_pos = BLUE_POS[:]
    if red_pos[1] == blue_pos[1] : # RED 와 BLUE가 같은 열에 있는지 확인
        if red_pos[0] < blue_pos[0]: # 행이 큰 쪽(BLUE) 먼저 이동
            moveBlueFirst(dir,red_pos,blue_pos)
        if blue_pos[0] < red_pos[0]: # 행이 큰 쪽(RED) 먼저 이동
            moveRedFirst(dir,red_pos,blue_pos)
    else:
        moveRedFirst(dir,red_pos,blue_pos)

def checkLeftward(dir):
    global RED_POS, BLUE_POS
    red_pos = RED_POS[:]
    blue_pos = BLUE_POS[:]
    if red_pos[0] == blue_pos[0] : # RED 와 BLUE가 같은 행에 있는지 확인
        if red_pos[1] < blue_pos[1]: # 열이 작은 쪽(RED) 먼저 이동
            moveRedFirst(dir,red_pos,blue_pos)
        if blue_pos[1] < red_pos[1]: # 열이 작은 쪽(BLUE) 먼저 이동
            moveBlueFirst(dir,red_pos,blue_pos)
    else:
        moveRedFirst(dir,red_pos,blue_pos)
def checkRightward(dir):
    global RED_POS, BLUE_POS
    red_pos = RED_POS[:]
    blue_pos = BLUE_POS[:]
    if red_pos[0] == blue_pos[0] : # RED 와 BLUE가 같은 행에 있는지 확인
        if red_pos[1] < blue_pos[1]: # 열이 큰 쪽(BLUE) 먼저 이동
            moveBlueFirst(dir,red_pos,blue_pos)
        if blue_pos[1] < red_pos[1]: # 열이 큰 쪽(RED) 먼저 이동
            moveRedFirst(dir,red_pos,blue_pos)
    else:
        moveRedFirst(dir,red_pos,blue_pos)
def tiltGrid(dir):

    if dir == 0: # 위방향
        checkUpward(dir)
        return

    if dir == 1: # 아래방향
        checkDownward(dir)
        return

    if dir == 2: # 좌측방향
        checkLeftward(dir)
        return

    if dir == 3: # 우측방향
        checkRightward(dir)
        return

def isValidTilt(): # Valid한지만 판단
    global RED_POS, BLUE_POS
    return BLUE_POS != CANDY_OUT

def isREDout():
    global RED_POS
    return RED_POS == CANDY_OUT

answer = 1e9
def dfs(cdir,cnt):

    global RED_POS, BLUE_POS, answer

    if not isValidTilt():
        return

    if isREDout():
        # printArr(grid)
        answer = min(answer,cnt)
        return

    if cnt > 10 :
        return

    for d in range(4):
        gridTemp = [
            row[:] for row in grid
        ]
        tempRED_POS, tempBLUE_POS = RED_POS, BLUE_POS
        tiltGrid(d)
        dfs(d,cnt+1)
        for i in range(N):
            for j in range(M):
                grid[i][j] = gridTemp[i][j]
        RED_POS, BLUE_POS = tempRED_POS, tempBLUE_POS


for k in range(4):
    gridTemp = [
        row[:] for row in grid
    ]
    tempRED_POS, tempBLUE_POS = RED_POS, BLUE_POS

    tiltGrid(k)
    dfs(k,1)

    for i in range(N):
        for j in range(M):
            grid[i][j] = gridTemp[i][j]
    RED_POS, BLUE_POS = tempRED_POS, tempBLUE_POS

if answer == 1e9:
    print(-1)
else:
    print(answer)
# for d in range(4):
#     print("curDir:",d)
#     gridTemp = [
#             row[:] for row in grid
#         ]
#     tempRED_POS, tempBLUE_POS = RED_POS, BLUE_POS
#     printArr(grid)
#
#     tiltGrid(d)
#
#     printArr(grid)
#
#     for i in range(N):
#         for j in range(M):
#             grid[i][j] = gridTemp[i][j]
#     RED_POS, BLUE_POS = tempRED_POS, tempBLUE_POS