N,M,H,K = list(map(int,input().split()))

def makeCurve(): # 술래가 움직일 루트

    # 시계 방향
    cx,cy,cd = N//2, N//2, -1 

    pathListClk = []
    for length in range(1,N+1): # 마지막 N개 버려야 함

        for _ in range(2):
            cd = (cd + 1) % 4
            for i in range(length):
                pathListClk.append((cx,cy,cd))
                cx, cy = cx + dxs[cd], cy + dys[cd]
    # 반 시계 방향
    
    cx,cy,cd = -1,N,4
    
    pathListCClk = []

    for length in range(N,0,-1):
        
        for _ in range(2):
            cd = (cd - 1) % 4
            for i in range(length):
                pathListCClk.append((cx,cy,cd))
                cx, cy = cx + dxs[cd], cy + dys[cd]

    return pathListClk[:-(N+1)] + pathListCClk[N+1:]

# 도망자
# 상하 유형 : 아래쪽 보고 시작
# 좌우 유형 : 오른쪽 보고 시작

# d : 1 --> 좌우,   0 --> 상하
#   오른쪽 보고 시작   아래쪽 보고 시작  
#        1             2
# 상 우 하 좌
dxs, dys = [-1,0,1,0],[0,1,0,-1]

runners = [
    tuple(map(int,input().split()))
    for _ in range(M)
]

trees = [
    tuple(map(int,input().split()))
    for _ in range(H)
]

runnerMap = [
    [[] for _ in range(N)]
    for _ in range(N)
]

treeMap = [
    [0] * N 
    for _ in range(N)
]

for rx,ry,rd in runners:
    if rd == 1 :
        runnerMap[rx-1][ry-1].append(1)
    else :
        runnerMap[rx-1][ry-1].append(2)

# Tree map
TREE = -1
chx,chy,chDir,cIdx = N//2, N//2, 0, 0
chaserRoute = makeCurve()
chaserScore = 0

for hx,hy in trees:
    treeMap[hx-1][hy-1] = TREE

def inRange(x,y):

    return 0<=x<N and 0<y<N

def moveRunners():

    nextRunnerMap = [
        [[] for _ in range(N)]
        for _ in range(N)
    ]

    for i in range(N):
        for j in range(N):
            if runnerMap[i][j]:
                cx,cy,curRunners = i,j,runnerMap[i][j][:]
                # 거리 3 이하인 도망자
                if abs(chx-i) + abs(chy-j) <= 3: 
                    for cd in curRunners:
                        nx, ny = cx + dxs[cd], cy + dys[cd]
                        if inRange(nx,ny):
                            # 가는 곳에 술래가 없으면
                            if (nx,ny) != (chx,chy):
                                nextRunnerMap[nx][ny].append(cd)
                            else: # 있으면
                                nextRunnerMap[cx][cy].append(cd)
                        else:
                            cd = (cd + 2) % 4
                            nx,ny = cx + dxs[cd], cy + dys[cd]
                            # 가는 곳에 술래가 없으면
                            if (nx,ny) != (chx,chy):
                                nextRunnerMap[nx][ny].append(cd)
                            else: # 있으면
                                nextRunnerMap[cx][cy].append(cd)
                else:
                    for cd in curRunners:
                        nextRunnerMap[cx][cy].append(cd)

    for i in range(N):
        for j in range(N):
            runnerMap[i][j] = nextRunnerMap[i][j][:]

def moveChaser():

    global chx,chy,chDir,cIdx
    
    cIdx = (cIdx + 1) % len(chaserRoute)

    chx,chy,chDir = chaserRoute[cIdx]

def catchRunners():
    global chaserScore
    dx,dy = dxs[chDir],dys[chDir]
    tx,ty = chx,chy    
    while True :
        tx,ty = tx + dx, ty+dy
        if inRange(tx,ty):
            if runnerMap[tx][ty] and treeMap[tx][ty] != TREE:
                chaserScore += turn * len(runnerMap[tx][ty])
                runnerMap[tx][ty] = []
        else:
            break

for turn in range(1,K+1):

    moveRunners()
    moveChaser()
    catchRunners()

print(chaserScore)