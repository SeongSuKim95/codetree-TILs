N, M = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

WALL = 6
# 1 -->
# <-- 2 -->
# ^        ^
# |        |
# 3 -->    4 -->
#          |
#          v
# 상 우 하 좌
dxs,dys = [-1,0,1,0],[0,1,0,-1]

types = {
    1 : [[0],[1],[2],[3]],
    2 : [[0,2],[1,3]],
    3 : [[0,1],[1,2],[2,3],[3,0]],
    4 : [[0,1,2],[1,2,3],[2,3,0],[0,1,3]],
    5 : [[0,1,2,3]]
} 

horsePos = []

HorseDirs = []

answer = 1e9

for i in range(N):
    for j in range(M):
        if grid[i][j] and grid[i][j]!= WALL:
            horsePos.append((i,j))

def inRange(x,y):
    
    return 0<=x<N and 0<=y<M

def getEmptySpace():

    newGrid = [
        row[:] for row in grid
    ]

    for curDirList,(chx,chy) in zip(HorseDirs,horsePos):

        for curDir in curDirList:
            dx,dy = dxs[curDir],dys[curDir]
            cx,cy = chx,chy
            while True :
                nx,ny = cx + dx, cy + dy
                if inRange(nx,ny):
                    if (newGrid[nx][ny] and newGrid[nx][ny] != WALL) or not newGrid[nx][ny]:
                        newGrid[nx][ny] = newGrid[cx][cy]
                        cx,cy = nx,ny
                    else :
                        break
                else :
                    break
    cnt = 0
    for i in range(N):
        for j in range(M):
            if newGrid[i][j] == 0 :
                cnt += 1
    return cnt 
            

def chooseDirs(hIdx):
    global answer

    if hIdx == len(horsePos) :
        answer = min(answer,getEmptySpace())
        return

    for dirs in types[grid[horsePos[hIdx][0]][horsePos[hIdx][1]]] :
        HorseDirs.append(dirs)
        chooseDirs(hIdx+1)
        HorseDirs.pop()
         
chooseDirs(0)      
print(answer)