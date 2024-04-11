import sys

def printArr(arr):

    for row in arr:
        print(*row)
    print()

def inRange(x,y):

    return 0<=x<4 and 0<=y<4

def canGo(x,y):

    return (x,y) != (px,py) and deadMap[x][y] == 0
def makeRoute(cnt):

    if cnt == 3 :
        packManRoute.append(selected[:])
        return

    for idx in range(4):
        selected.append(idx)
        makeRoute(cnt+1)
        selected.pop()

# sys.stdin = open('input.txt', 'r')

M, T = list(map(int, sys.stdin.readline().split()))

px,py = list(map(lambda x : int(x) - 1, sys.stdin.readline().split()))

# monster 방향
mdirs = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
# packman 방향
# 상 좌 하 우
pdirs = [(-1,0),(0,-1),(1,0),(0,1)]

monsters = [
    tuple(map(lambda x : int(x) - 1, sys.stdin.readline().split()))
    for _ in range(M)
]

# 각 몬스터의 direction을 표시
monsterMap = [
    [[] for _ in range(4)]
    for _ in range(4)
]

for mx,my,md in monsters:

    monsterMap[mx][my].append(md)

# 시체의 소멸시까지 남은 시간을 표시
deadMap = [
    [0 for _ in range(4)]
    for _ in range(4)
]
# 현재 알의 direction 을 표시 (다음 턴에 부화)
eggMap = [
    [[] for _ in range(4)]
    for _ in range(4)
]

packManRoute = []
selected = []

makeRoute(0)

def makeEggs():

    for i in range(4):
        for j in range(4):
            if monsterMap[i][j] != []:
                eggMap[i][j] = monsterMap[i][j][:]

def moveMonsters():

    nextMonsterMap = [
        [[] for _ in range(4)]
        for _ in range(4)
    ]

    for i in range(4):
        for j in range(4):
            if monsterMap[i][j] != []:
                cx,cy = i,j
                for md in monsterMap[i][j]:
                    Flag = False
                    for r in range(8): # 8방향 탐색
                        cd = (md + r + 8) % 8
                        dx,dy = mdirs[cd]
                        nx,ny = cx + dx, cy + dy
                        if inRange(nx,ny) and canGo(nx,ny):
                            nextMonsterMap[nx][ny].append(cd)
                            Flag = True
                            break
                    if not Flag: # 못가는 경우 그대로
                        nextMonsterMap[cx][cy].append(md)

    for i in range(4):
        for j in range(4):
            monsterMap[i][j] = nextMonsterMap[i][j][:]
def clearDead():

    for i in range(4):
        for j in range(4):
            if deadMap[i][j] :
                deadMap[i][j] -= 1

def countMonsters():
    cnt = 0
    for i in range(4):
        for j in range(4):
           if monsterMap[i][j] != []:
               cnt += len(monsterMap[i][j])
    return cnt
def eggBirth():

    for i in range(4):
        for j in range(4):
            if eggMap[i][j] != []:
                for cd in eggMap[i][j]:
                    monsterMap[i][j].append(cd)
    # eggMap 초기화
    for i in range(4):
        for j in range(4):
            eggMap[i][j] = []
def movePackman():
    global px,py
    # pdirs = [(-1,0),(0,-1),(1,0),(0,1)]
    routeResults = []

    for idx,moveOrder in enumerate(packManRoute):
        tempMonsterMap = [
            [monsterMap[i][j][:] for j in range(4)]
            for i in range(4)
        ]
        curOrder = moveOrder[:]

        cx,cy,curSum,Flag = px,py,0,False
        for cd in curOrder:
            nx, ny = cx + pdirs[cd][0], cy + pdirs[cd][1]
            if not inRange(nx,ny): # 이동 도중 격자 벗어날 시 고려 안함
                Flag = True
                break
            if tempMonsterMap[nx][ny] != []:
                curSum += len(tempMonsterMap[nx][ny])
                tempMonsterMap[nx][ny] = []
            cx,cy = nx,ny

        if not Flag: # 끝까지 간 경우에 대해
            routeResults.append((curSum,-idx))

    _ , routeIdx = max(routeResults)

    selectedRoute = packManRoute[-routeIdx]

    for sDir in selectedRoute:
        px,py = px + pdirs[sDir][0] , py + pdirs[sDir][1]
        if monsterMap[px][py] != []:
            deadMap[px][py] = 3 # 두턴 유효
        monsterMap[px][py] = [] # monster 잡아먹기

# mdirs = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
for _ in range(T):
    makeEggs()
    moveMonsters()
    movePackman()
    clearDead()
    eggBirth()

print(countMonsters())