# 격자 크기, 플레이어수 , 라운드 수
N,M,K = list(map(int,input().split()))

guns = [
    list(map(int,input().split()))
    for _ in range(N)
]

GUN_EMPTY = [0]
NO_GUN = 0

# (x,y), d, s 
# 위치, 방향, 초기 능력치
players = [
    tuple(map(int,input().split()))
    for _ in range(M)
]
# 상 우 하 좌
dxs, dys = [-1,0,1,0], [0,1,0,-1]

# 1. 각 칸의 총 상태를 표기하기 위한 배열

gunMap = [
    [[] for _ in range(N)]
    for _ in range(N)
]

for i in range(N):
    for j in range(N):
        gunMap[i][j].append(guns[i][j])

# 2. 플레이어 위치를 표기할 배열 (번호, 방향, 기본 스탯, 총의 공격력(없으면 0))
# 플레이어가 겹칠수도 있으므로, 배열로 처리
playerMap = [
    [[] for _ in range(N)]
    for _ in range(N)
]

playerPos = {}

playerScore = {}

for idx,(px,py,pd,ps) in enumerate(players):
    # 초기엔 총 없음
    playerMap[px-1][py-1].append((idx+1,pd,ps,0))
    playerPos[idx+1] = (px-1,py-1)
    playerScore[idx+1] = 0

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def getGun(pos,pidx,pd,ps,pgun):

    nx,ny = pos
    if gunMap[nx][ny] != GUN_EMPTY : 
        totalGunList = sorted(gunMap[nx][ny] + [pgun],reverse = True)
        pgun = totalGunList[0] # 가장 쎈 gun
        if len(totalGunList[1:]) :
            gunMap[nx][ny] = totalGunList[1:][:]
        else :
            gunMap[nx][ny] = GUN_EMPTY
    playerMap[nx][ny].append((pidx,pd,ps,pgun))

def moveOnePlayer(pIdx):

    px,py = playerPos[pIdx]
    
    pidx,pd,ps,pgun = playerMap[px][py][0] # List 이므로

    nx,ny = px + dxs[pd], py + dys[pd]


    if not inRange(nx,ny):
        pd = ( pd + 2 ) % 4
        nx,ny = px + dxs[pd], py + dys[pd]
    
    # 이전 자리 비우기
    playerMap[px][py] = []

    # 옮긴 자리에 사람이 없다면 총 들기
    if playerMap[nx][ny] == [] : # 다른 플레이어가 없다면
        npos = (nx,ny)
        # 총이 있는 경우 총 획득
        getGun(npos,pidx,pd,ps,pgun)
        playerPos[pidx] = npos

    else : # 다른 플레이어가 있다면
        
        nidx,nd,ns,ngun = playerMap[nx][ny][0] # 간 자리에 있는 player
        curPlayerSpec, nextPlayerSpec = (ps+pgun,ps,pidx,pd,pgun), (ns+ngun,ns,nidx,nd,ngun)
        winnerPlayerSpec,loserPlayerSpec = max(curPlayerSpec,nextPlayerSpec), min(curPlayerSpec,nextPlayerSpec)
        # 승자,패자 정보
        _ ,winnerStat,winnerPidx,winnerDir,winnerGun = winnerPlayerSpec
        _ ,loserStat,loserPidx,loserDir,loserGun = loserPlayerSpec
        # score 반영
        playerScore[winnerPidx] += abs(winnerPlayerSpec[0] - loserPlayerSpec[0]) # 능력치 + 총의 공격력 차이
        # 패자 행동
        # 1. 총 내려놓기
        if loserGun:
            gunMap[nx][ny].append(loserGun)
        
        for i in range(4):
            nnd = (loserDir + i) % 4
            nnx,nny = nx + dxs[nnd], ny + dys[nnd]
            if inRange(nnx,nny) and playerMap[nnx][nny] == []:
                nnpos = nnx,nny
                getGun(nnpos,loserPidx,nnd,loserStat,0)
                playerPos[loserPidx] = nnpos
                break

        # 승자 행동
        # 1. 가장 좋은 총 들고, 나머지 총 내려놓기
        winnerPos = (nx,ny)
        playerMap[nx][ny] = []
        getGun(winnerPos,winnerPidx,winnerDir,winnerStat,winnerGun)
        playerPos[winnerPidx] = winnerPos

def printArr(arr):

    for row in arr:
        print(*row)
    print()

def simulate():
    for i in range(K):
        
        # print("Turn",i+1)
        for pIdx in range(1,M+1):
            moveOnePlayer(pIdx)
        # printArr(playerMap)
        # printArr(gunMap)
        # print(playerPos)
        print(*list(playerScore.values()))

simulate()