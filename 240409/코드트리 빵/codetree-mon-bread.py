from collections import deque
# 03:50

# m분에 m번사람이 베이스캠프에 들어감

# 이동 방향 우선순위 --> 상 좌 우 하
# 편의점에서부터 찾기 --> 하 우 좌 상

dxs,dys = [1,0,0,-1],[0,1,-1,0]


# bfs로 베이스캠프에 도착 하는 케이스 발견시 바로 리턴 

# N : 격자의 크기, M : 사람의 수

def printArr(arr):

    for row in arr:
        print(*row)
    print()

N, M = list(map(int,input().split()))

BASECAMP = -1
BLOCKED = -2

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

for i in range(N):
    for j in range(N):
        if grid[i][j]: 
            grid[i][j] = BASECAMP

stores = [
    tuple(map(lambda x :int(x)-1,input().split()))
    for _ in range(M)
]

storePos = {}
personPos = {}

for idx,(sx,sy) in enumerate(stores):
    grid[sx][sy] = idx + 1
    storePos[idx+1] = (sx,sy)

# 현재 사람이 있는 위치에 사람 번호 적기
personMap = [
    [0] * N 
    for _ in range(N)
]

def allArrived():

    for pIdx,(sx,sy) in storePos.items():
        if pIdx != personMap[sx][sy]:
            return False
 
    return True

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def findRoute(pIdx,px,py):
    dist = [
        [0] *N
        for _ in range(N)
    ]
    
    q = deque()
    sx,sy = storePos[pIdx]
    dist[sx][sy] = 1
    q.append((sx,sy))
    
    while q : # store에서부터 출발
        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cx+dx,cy+dy
            if inRange(nx,ny) and not dist[nx][ny] :
                if grid[nx][ny] != BLOCKED or (nx,ny) == (px,py):
                    q.append((nx,ny))
                    dist[nx][ny] = dist[cx][cy] + 1
                    if (nx,ny) == (px,py) :
                        return (cx,cy)


def findRouteAll():
    # 이동 불가 표시는 grid에

    nextPoses = []
    for pIdx,(px,py) in personPos.items():
        npx,npy = findRoute(pIdx,px,py)
        nextPoses.append((pIdx,npx,npy))

    for nextPose in nextPoses:
        pIdx,npx,npy = nextPose
        cpx,cpy = personPos[pIdx]
        personMap[cpx][cpy] = 0
        personMap[npx][npy] = pIdx
        personPos[pIdx] = (npx,npy)
        sx,sy = storePos[pIdx]
        if (npx,npy) == (sx,sy):
            personPos.pop(pIdx)
            personMap[sx][sy] = pIdx
            grid[sx][sy] = BLOCKED

def goToBaseCamp(pIdx):

    dist = [
        [0] * N
        for _ in range(N)
    ]

    q = deque()
    sx,sy = storePos[pIdx]
    q.append((sx,sy))
    dist[sx][sy] = 1

    baseCampList = []

    while q:
        cx,cy = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx,ny = cx+dx, cy+dy
            if inRange(nx,ny) and not dist[nx][ny] and grid[nx][ny] != BLOCKED:
                dist[nx][ny] = dist[cx][cy] + 1
                q.append((nx,ny))
                if grid[nx][ny] == BASECAMP :
                    baseCampList.append((dist[nx][ny],nx,ny))

    dist,bx,by = min(baseCampList)
    personMap[bx][by] = pIdx
    grid[bx][by] = BLOCKED
    personPos[pIdx] = (bx,by)

def simulate():

    elapsedTime = 0

    while True:

        if allArrived():
            return elapsedTime

        elapsedTime += 1
        # 1초인 경우
        if elapsedTime == 1 :
            goToBaseCamp(elapsedTime)
            continue
        # 사람이 있으면, 가고 싶은 편의점을 향해서 1칸 움직임 , 상 좌 우 하 우선순위
        findRouteAll()
        # 편의점에 도착하면 해당 편의점에서 멈추고, 다른 사람들은 칸을 지나가지 못함. 격자에 있는 사람들이 모두 이동한 후에 업데이트
        # t <= M 이면 t번 사람이 가장 가까이 있는 베이스 캠프에 들어감
        if elapsedTime <= M :
            goToBaseCamp(elapsedTime)
        
    return elapsedTime

print(simulate())