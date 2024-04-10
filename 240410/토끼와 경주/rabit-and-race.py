from collections import defaultdict

N, M = 0,0
# 상 우 하 좌
dirs = [(-1,0),(0,1),(1,0),(0,-1)]
rabbitSpecs = defaultdict(tuple)
rabbitScore = defaultdict(int)
def inRange(x,y):

    return 0<=x<N and 0<=y<M

def init(datas):
    global N,M
    initCode, initN, initM, P  = datas[:4]
    N, M = initN, initM
    rabbitInfos = datas[4:]
    initRx, initRy, initJumpCnt = 0,0,0
    for pIdx in range(0,2 * P,2):
        curIdx, curDist = rabbitInfos[pIdx], rabbitInfos[pIdx+1]
        rabbitSpecs[curIdx] = (initJumpCnt, initRx + initRy, initRx, initRy, curIdx, curDist)
        rabbitScore[curIdx] = 0

def moveRabbits(datas):
    # K : turn 수, S : 턴 끝났을 때 점수
    K, S = datas

    for i in range(K):
        sortedRabbits = sorted(rabbitSpecs.items(), key=lambda x: x[1])[:]  # value 기준 sorting
        cIdx,curRabbitSpecs = sortedRabbits[0]
        curJumpCnt, _, cx,cy,cIdx,cDist = curRabbitSpecs
        ox,oy = cx,cy
        posList = []
        for dIdx in range(4):
            cd,cx,cy = dIdx,ox,oy
            dx,dy = dirs[cd]
            for _ in range(cDist):
                nx, ny = cx + dx, cy + dy
                if not inRange(nx,ny):
                    cd = (cd + 2) % 4
                    dx,dy = dirs[cd]
                    nx, ny = cx + dx, cy + dy
                cx,cy = nx,ny
            posList.append((cx+cy,cx,cy))
        _, nextx,nexty = max(posList)
        rabbitSpecs[cIdx] = (curJumpCnt+1,nextx+nexty,nextx,nexty,cIdx,cDist)

        for rIdx, _ in sortedRabbits[1:]:
            rabbitScore[rIdx] += nextx + nexty + 2
    #  (현재 서있는 행 번호 + 열 번호가 큰 토끼, 행 번호가 큰 토끼, 열 번호가 큰 토끼, 고유번호가 큰 토끼) 순으로 우선순위를 두었을 때 우선 순위 높은 토끼에 S 부여
    winnerRabbit = sorted(rabbitSpecs.items(), key=lambda x: x[1][1:5],reverse=True)[0][1][4]
    rabbitScore[winnerRabbit] += S

def changeDistance(datas):

    rIdx, scale = datas
    curJumpcnt, posSum, cx, cy, cIdx, cDist = rabbitSpecs[rIdx]
    rabbitSpecs[rIdx] = (curJumpcnt, posSum, cx, cy, cIdx, cDist * scale)

def finish():

    return max(rabbitScore.values())

def simulate():
    for _ in range(Q-1):
        datas = list(map(int, input().split()))
        code = datas[0]

        if code == 200 :
            moveRabbits(datas[1:])
        elif code == 300:
            changeDistance(datas[1:])
        elif code == 400:
            max_score = finish()
            return max_score

Q = int(input())

initData = list(map(int, input().split()))
init(initData)
print(simulate())