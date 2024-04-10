import sys
from collections import deque

# N X M , K 턴
N, M, K = list(map(int, sys.stdin.readline().split()))

DESTROYED = 0

grid = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(N)
]

lastActivated = [
    [0] * M
    for _ in range(N)
]

back_x = [
    [0] * M
    for _ in range(N)
]

back_y = [
    [0] * M
    for _ in range(N)
]

usedTurrets = [
    [False] * M
    for _ in range(N)
]


def printArr(arr):

    for row in arr:
        print(*row)
    print()
def chooseTurrets():

    turretList = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] != DESTROYED:
                # (공격력, 최근 공격 turn, 행과 열의 합, 열)
                # 공격력 낮을 수록
                # 최근 공격 turn이 클수록
                # 행과 열의 합이 클수록
                # 열의 크기가 클수록
                turretList.append((grid[i][j],-lastActivated[i][j],-(i+j),-j,-i))
    _,_,_,ay,ax = min(turretList)
    _,_,_,ty,tx = max(turretList)
    return (-ax,-ay), (-tx,-ty)

def findRoute(attacker,target): # 경로가 있으면 경로를 반환, 없으면 false 반환
    # 이동 우선 순위
    dxs,dys = [0,1,0,-1],[1,0,-1,0]

    ax,ay = attacker
    tx,ty = target

    visited = [
        [0] * M
        for _ in range(N)
    ]

    for i in range(N):
        for j in range(M):
            back_x[i][j], back_y[i][j] = 0, 0

    q = deque([(ax,ay)])
    visited[ax][ay] = 1
    while q :
        cx, cy = q.popleft()
        for idx,(dx, dy) in enumerate(zip(dxs,dys)):
            nx, ny = (cx + dx + N) % N, (cy + dy + M ) % M
            if grid[nx][ny] != DESTROYED and visited[nx][ny] == 0:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))
                back_x[nx][ny] = cx
                back_y[nx][ny] = cy
                if (nx,ny) == (tx,ty):
                    return True
    return False

def destroyTurrets():

    for i in range(N):
        for j in range(M):
            if grid[i][j] <= 0:
                grid[i][j] = DESTROYED

def healTurrets():
    # printArr(usedTurrets)
    # printArr(grid)
    for i in range(N):
        for j in range(M):
            if grid[i][j] != DESTROYED and not usedTurrets[i][j]:
                grid[i][j] += 1

def LaserAttack(attacker,target):

    for i in range(N):
        for j in range(M):
            usedTurrets[i][j] = False

    # 공격 포탑 정보
    ax,ay = attacker
    usedTurrets[ax][ay] = True
    grid[ax][ay] += N + M
    damage = grid[ax][ay]
    # target 포탑 정보
    tx,ty = target
    grid[tx][ty] -= damage
    usedTurrets[tx][ty] = True

    # 경로에 있는 포탑 : damage의 절반
    cx,cy = back_x[tx][ty],back_y[tx][ty]
    while True:
        if (cx,cy) == (ax,ay):
            break
        grid[cx][cy] -= damage // 2
        usedTurrets[cx][cy] = True
        cx,cy = back_x[cx][cy],back_y[cx][cy]

def bombAttack(attacker,target):

    for i in range(N):
        for j in range(M):
            usedTurrets[i][j] = False
    # 공격 포탑 정보
    ax,ay = attacker
    usedTurrets[ax][ay] = True
    grid[ax][ay] += N + M
    damage = grid[ax][ay]
    # target 포탑 정보
    tx,ty = target
    grid[tx][ty] -= damage
    usedTurrets[tx][ty] = True

    # 8방에 damage의 반만큼 영향
    dxs,dys = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]
    for dx,dy in zip(dxs,dys):
        nx,ny = (tx + dx + N) % N, (ty + dy + M) % M
        if grid[nx][ny] != DESTROYED:
            grid[nx][ny] -= damage // 2
            usedTurrets[nx][ny] = True

def attack(attacker,target):

    if findRoute(attacker,target):
        LaserAttack(attacker,target)
        destroyTurrets()
        healTurrets()
    else :
        bombAttack(attacker,target)
        destroyTurrets()
        healTurrets()

def getStrongestTurret():

    maxTurret = -1
    for i in range(N):
        for j in range(M):
            maxTurret = max(maxTurret,grid[i][j])
    return maxTurret
def simulate():

    for turn in range(1,K+1):
        attacker, target = chooseTurrets()
        ax,ay = attacker
        lastActivated[ax][ay] = turn
        attack(attacker,target)
    print(getStrongestTurret())

simulate()