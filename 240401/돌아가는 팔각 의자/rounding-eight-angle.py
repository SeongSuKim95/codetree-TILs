# 0 북, 1 남

tables = [[]] + [
    list(map(int,input()))
    for _ in range(4)
]

k = int(input())

# (table 번호, 방향 1: 시계 -1 : 반시계)
turns = [
    tuple(map(int,input().split())) for _ in range(k)
]

def tableTurn(tableNum,dir):
    curTable = tables[tableNum]
    if dir == 1: # clockWise
        tables[tableNum] = [curTable[-1]] + curTable[:-1] 
    elif dir == -1 : # counterClock 
        tables[tableNum] = curTable[1:] + [curTable[0]]

def turnEachTables(tableIdx,dir):
    Results = [0] * 5 # curIdx + 1 ~ 4 까지의 정보 기록용
    Results[tableIdx] = dir

    # 현재 테이블의 9시 방향 사람 : tables[curIdx][2]
    # 오른쪽 테이블의 3시 방향 사람 : tables[curIdx+1][6]
    # 같으면 회전 하지 않음 --> break
    # 다르면 반대 방향 회전, 그 이후 테이블의 상태까지 봐야함
    curDir = dir
    for idx in range(tableIdx,4):
        curPeople3,nextpeople9 = tables[idx][2],tables[idx+1][6]
        if curPeople3 == nextpeople9: break
        nextDir,nextIdx = curDir * (-1), idx + 1
        Results[nextIdx] = nextDir
        curDir = nextDir
    # 현재 테이블의 9시 방향 사람 : tables[curIdx][6]
    # 왼쪽 테이블의 3시 방향 사람 : tables[curIdx-1][2]
    # 같으면 회전 하지 않음 --> break
    # 다르면 반대 방향 회전, 그 이후 테이블의 상태까지 봐야함
    curDir = dir
    for idx in range(tableIdx,1,-1):
        curPeople9,nextpeople3 = tables[idx][6],tables[idx-1][2]
        if curPeople9 == nextpeople3: break
        nextDir,nextIdx = curDir * (-1), idx -1
        Results[nextIdx] = nextDir
        curDir = nextDir

    for tablenum in range(1,5):
        curdir = Results[tablenum] 
        tableTurn(tablenum,curdir)

def simulate():
    answer = 0
    for tableIdx,dir in turns:
        turnEachTables(tableIdx,dir)
    for i in range(1,5):
        answer += tables[i][0] * 2 ** (i-1)
    return answer

print(simulate())