import sys
from collections import defaultdict
# sys.stdin = open('input.txt','r')

# 5:20 까지

# (5) 상호작용
#
# 루돌프와의 충돌 후 산타는 포물선의 궤적으로 이동하여 착지하게 되는 칸에서만 상호작용이 발생할 수 있습니다.
# 산타는 충돌 후 착지하게 되는 칸에 다른 산타가 있다면 그 산타는 1칸 해당 방향으로 밀려나게 됩니다. 그 옆에 산타가 있다면 연쇄적으로 1칸씩 밀려나는 것을 반복하게 됩니다. 게임판 밖으로 밀려나오게 된 산타의 경우 게임에서 탈락됩니다.

# 격자 크기, 턴 수, 산타 수, 루돌프 힘, 산타 힘
N, M, P, C, D = list(map(int,sys.stdin.readline().split()))
Rx,Ry = list(map(int,sys.stdin.readline().split()))
Rx,Ry = Rx-1, Ry-1
# 루돌프 8방, 산타 4방
Rdirs = [(-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1)]
Sdirs = [(-1,0),(0,1),(1,0),(0,-1)] # 상 우 하 좌

def printArr(arr):

    for row in arr:
        print(*row)
    print()

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def getDist(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    return abs((x1-x2)**2+(y1-y2)**2)

# (산타 번호, 산타 x, 산타 y)
santaPos = [
    tuple(map(int,sys.stdin.readline().split()))
    for _ in range(P)
]

# 매턴 업데이트 대상
santaInfo = defaultdict(tuple)
santaMap = [
    [[] for _ in range(N)]
    for _ in range(N)
]

santaScore = {}

for idx,sx,sy in santaPos:
    santaMap[sx-1][sy-1].append(idx)
    santaInfo[idx] = (sx-1,sy-1,0) # 기절 시간, 격자 밖을 나간 경우 -1 , 기절 안한 경우 0
    santaScore[idx] = 0

SANTA_OUT = -1


def getAliveSanta():
    currSanta = []
    for sidx,(sx,sy,stunTime) in santaInfo.items():
        if stunTime != SANTA_OUT : # 기절한 산타 포함
            currSanta.append((sidx,sx,sy))
    return currSanta

def moveRudolf():
    global Rx,Ry

    # 현재 살아 있는 산타 리스트
    currSantaInfo= getAliveSanta()
    santaDists = []
    # 현재 살아 있는 산타들과 루돌프간 거리 구하기
    for sidx,sx,sy in currSantaInfo:
        curDist = (getDist((Rx,Ry),(sx,sy)),-sx,-sy)
        santaDists.append(curDist)

    # 최소 거리 산타
    minSantaIdx, minSx, minSy = min(santaDists)
    minSx, minSy = -minSx,-minSy # 부호 전환

    # 루돌프가 8방향 중 해당 가장 가까운 방향으로 돌진
    minSantaDists = []
    for Rdir in Rdirs:
        dx,dy = Rdir
        nRx,nRy = dx + Rx, dy + Ry
        if inRange(nRx,nRy):
            minSantaDists.append((getDist((nRx,nRy),(minSx,minSy)),dx,dy))
    # 가장 가까워지는 방향
    _, Rdx, Rdy = min(minSantaDists)
    # 루돌프 위치 update
    sRx,sRy = Rx, Ry
    Rx, Ry = Rx + Rdx, Ry + Rdy

    # 루돌프가 산타와 ( 산타 기절, 산타 OUT 에 따른 산타 상태 update)
    if len(santaMap[Rx][Ry]) != 0: # 옮긴 루돌프의 위치에 산타가 있으면 충돌
        sIdx = santaMap[Rx][Ry][0]
        santaCollision(sIdx,(sRx,sRy),(Rx,Ry),(Rdx,Rdy))
def santaCollision(sIdx,spos,epos,rdir):
    global Rx,Ry,C,D

    santaScore[sIdx] += C
    sx,sy = epos
    rdx,rdy = rdir
    # 반대 방향 으로 C만큼 튕겨 나감
    nsx,nsy = sx + C * rdx, sy + C * rdy
    # 1. 격자를 벗어나는 경우
    if not inRange(nsx,nsy):
        santaMap[sx][sy].remove(sIdx)
        santaInfo[sIdx] = (nsx,nsy,-1)
        return
    # 2. 해당 자리에 다른 산타가 있는 경우
    if len(santaMap[nsx][nsy]) != 0 : # 루돌프와 충돌한 산타는 기절, 옆에 있는 산타는 방향대로 1칸씩 연쇄적으로 밀려남
        chainCollsion((rdx,rdy),sIdx,(sx,sy),(nsx,nsy))
        return
    # 3. 빈칸인 경우 스턴
    if len(santaMap[nsx][nsy]) == 0 :
        santaMap[sx][sy].remove(sIdx)
        santaMap[nsx][nsy].append(sIdx)
        santaInfo[sIdx] = (nsx,nsy,2) # 스턴 시간 update
        return
def chainCollsion(dir,sIdx,spos,epos): # 방향, 처음 산타 출발점

    cx,cy = spos
    ex,ey = epos
    dx,dy = dir
    # 이전 산타 원래 위치 정보 업데이트
    santaMap[cx][cy].remove(sIdx)
    # 산타 있는 상황임!!!!!
    tIdx = santaMap[ex][ey].pop()
    santaMap[ex][ey].append(sIdx)
    santaInfo[sIdx] = (ex,ey,2) # 충돌 후 기절

    while True :
        sIdx = tIdx
        nex, ney = ex + dx, ey + dy
        if not inRange(nex,ney): # 범위가 아닐 경우
            santaInfo[tIdx] = (nex,ney,-1) # 팅겨 나감 반영
            return
        if inRange(nex,ney): # 범위 내일 경우

            if len(santaMap[nex][ney]) == 0 :# 빈칸인 경우
                santaMap[nex][ney].append(sIdx)
                tsantaInfo = santaInfo[sIdx]
                santaInfo[sIdx] = (nex,ney,tsantaInfo[2])
                return

            if santaMap[nex][ney] : # 다른 산타 있는 경우

                tIdx = santaMap[nex][ney].pop()
                santaMap[nex][ney].append(sIdx)

                tsantaInfo = santaInfo[sIdx]
                santaInfo[sIdx] = (nex,ney,tsantaInfo[2])
                ex, ey = nex, ney
def rudolfCollision(sIdx,cpos,npos,sdir):
    global Rx,Ry,C,D
    # cx, cy : 이동 전 지점
    cx,cy = cpos
    # sx, sy : 이동한 지점 (충돌 지점)
    sx,sy = npos
    # sdir : 이동시 방향

    # 산타 스코어 update
    santaScore[sIdx] += D

    sdx,sdy = sdir
    # 반대 방향 으로 D만큼 튕겨 나감
    sdx,sdy = -sdx,-sdy
    nsx,nsy = sx + D * sdx, sy + D * sdy
    # 1. 격자를 벗어나는 경우
    if not inRange(nsx,nsy):
        santaMap[cx][cy].remove(sIdx)
        santaInfo[sIdx] = (nsx,nsy,-1)
        return
    # 2. 해당 자리에 다른 산타가 있는 경우
    if len(santaMap[nsx][nsy]) != 0 : # 루돌프와 충돌한 산타는 기절, 옆에 있는 산타는 방향대로 1칸씩 연쇄적으로 밀려남
        chainCollsion((sdx,sdy),sIdx,cpos,(nsx,nsy))
        return
    # 3. 빈칸인 경우 스턴
    if len(santaMap[nsx][nsy]) == 0 :
        santaMap[cx][cy].remove(sIdx)
        santaMap[nsx][nsy].append(sIdx)
        santaInfo[sIdx] = (nsx,nsy,2) # 스턴 시간 update
        return
def moveOneSanta(sIdx):

    # 1번 부터 P번 까지 순서대로
    # 기절한 산타, 탈락한 산타 못 움직임
    # 산타는 루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동합니다.
    # 산타는 다른 산타가 있는 칸이나 게임판 밖으로는 움직일 수 없습니다.
    # 움직일 수 있는 칸이 없다면 산타는 움직이지 않습니다.
    # 움직일 수 있는 칸이 있더라도 만약 루돌프로부터 가까워질 수 있는 방법이 없다면 산타는 움직이지 않습니다.
    # 산타는 상하좌우로 인접한 4방향 중 한 곳으로 움직일 수 있습니다. 이때 가장 가까워질 수 있는 방향이 여러 개라면, 상우하좌 우선순위에 맞춰 움직입니다.
    cx, cy, cStunTime = santaInfo[sIdx]

    if cStunTime > 0 or cStunTime == SANTA_OUT: # 기절 혹은 OUT
        return
    # 현재 루돌프와 산타간 거리
    currDist = getDist((Rx,Ry),(cx,cy))

    # 4방향에 대한 루돌프와의 거리를 저장
    rudolfDists = []

    for dIdx, sdir in enumerate(Sdirs):
        dx,dy = sdir
        ncx,ncy = cx+dx, cy+dy
        if not inRange(ncx,ncy) :# 격자 밖이거나
            continue
        if len(santaMap[ncx][ncy]) > 0 : # 다른 산타가 있으면 계산 X
            continue
        rudolfDists.append((getDist((Rx,Ry),(ncx,ncy)),dIdx))
    # 움직일 수 있는 방향이 없는 경우
    if len(rudolfDists) == 0:
        return
    # 루돌프와 가장 가까워 질때의 최소 거리, 방향 Idx
    minDist , minDirIdx = min(rudolfDists)

    if minDist == currDist : # 더 가까워질 방법이 없는 경우
        return

    # santa 정보 업데이트
    nsx,nsy = cx + Sdirs[minDirIdx][0], cy + Sdirs[minDirIdx][1]
    # 루돌프와 충돌 시 처리 해야함.
    if (nsx,nsy) == (Rx,Ry): # 옮긴 산타의 위치에 루돌프가 있으면 # 충돌
        rudolfCollision(sIdx,(cx,cy),(nsx,nsy),Sdirs[minDirIdx])
    else:
        santaMap[cx][cy].remove(sIdx) # 이전 산타 정보 지우기
        santaMap[nsx][nsy].append(sIdx) # 새로운 위치에 산타 정보 추가
        santaInfo[sIdx] = (nsx,nsy,cStunTime) # TODO : cStunTume update
def turnAction():

    for sIdx, (sx,sy,stuntime) in santaInfo.items():
        if stuntime != SANTA_OUT:
            santaScore[sIdx] += 1
        if stuntime > 0 :
            santaInfo[sIdx] = (sx,sy,stuntime-1) # stun 시간 1 줄이기

for _ in range(M):
    moveRudolf()
    for i in range(1,P+1):
        moveOneSanta(i)
    turnAction()
    # print(Rx,Ry)
    # printArr(santaMap)
    # print(santaInfo)
print(*santaScore.values())