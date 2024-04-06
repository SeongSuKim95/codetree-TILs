N,M,t = list(map(int,input().split()))

EMPTY = 0
HURRICANE = -1

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

dxs,dys = [-1,1,0,0],[0,0,-1,1]
upperPos, lowerPos = 0,0 

def findHurricane():
    global upperPos, lowerPos
    pos = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == HURRICANE:
                pos.append((i,j))
    upperPos, lowerPos = pos[0], pos[1]

def inRange(x,y):

    return 0<=x<N and 0<=y<M

def printArr(arr):

    for row in arr:
        print(*row)
    print()

# 먼지 확산
# - 인접한 4 방향에 대해서 벽이 아니거나 / 돌풍이 없는 경우, 확산되는 먼지는 원래 칸에 있는 먼지를 5로 나눈 값
# - 소숫점 버리고, 원래 칸에서 확산된 먼지 합 만큼 뺌
# - 모든 칸 전부 반영되고 업데이트
 
def spread():
    global upperPos,lowerPos

    newGrid = [
        [EMPTY] * M 
        for _ in range(N)
    ]
    
    newGrid[upperPos[0]][upperPos[1]], newGrid[lowerPos[0]][lowerPos[1]] = -1,-1

    for i in range(N):
        for j in range(M):
            cx,cy = i,j
            if grid[cx][cy] !=  HURRICANE and grid[cx][cy]:
                newGrid[cx][cy] += grid[cx][cy] # 원래 값부터 더해주기
                for dx,dy in zip(dxs,dys):
                    nx,ny = cx + dx ,cy + dy
                    if inRange(nx,ny) and grid[nx][ny] != HURRICANE:
                        newGrid[nx][ny] += grid[cx][cy] // 5
                        newGrid[cx][cy] -= grid[cx][cy] // 5
 
            elif grid[cx][cy] == HURRICANE:
                newGrid[cx][cy] = HURRICANE
 
    for i in range(N):
        for j in range(M):
            grid[i][j] = newGrid[i][j]

def clean():

    global upperPos,lowerPos

    newGrid = [
        row[:]
        for row in grid
    ]
    
    newGrid[lowerPos[0]][lowerPos[1]] = -1

    # 위 돌풍 반시계 방향 테두리 회전
    # 하변
    ux,uy = upperPos
    for col in range(M-2,0,-1):
        newGrid[ux][col+1] = grid[ux][col]
    # 우변
    for row in range(1,ux+1):
        newGrid[row-1][M-1] = grid[row][M-1]
    # 상변
    for col in range(1,M):
        newGrid[0][col-1] = grid[0][col]
    # 좌변 
    for row in range(ux-1,-1,-1):
        newGrid[row+1][0] = grid[row][0]
    
    newGrid[upperPos[0]][upperPos[1]] = -1
    newGrid[upperPos[0]][upperPos[1]+1] = 0

    # 아래 돌풍 시계 방향 테두리 회전
    # 상변
    lx,ly = lowerPos
    for col in range(M-2,0,-1):
        newGrid[lx][col+1] = grid[lx][col]
    # 우변
    for row in range(N-2,lx-1,-1):
        newGrid[row+1][M-1] = grid[row][M-1]
    # 하변
    for col in range(1,M):
        newGrid[N-1][col-1] = grid[N-1][col]
    # 좌변 
    for row in range(lx+1,N):
        newGrid[row-1][0] = grid[row][0]
    
    newGrid[lowerPos[0]][lowerPos[1]] = -1
    newGrid[lowerPos[0]][lowerPos[1]+1] = 0

    for i in range(N):
        for j in range(M):
            grid[i][j] = newGrid[i][j]
findHurricane()
for i in range(t):
    # print(t)
    spread()
    # print("After spread")
    # printArr(grid)
    clean()
    # print("After Cleaned")
    # printArr(grid)

print(sum(
    grid[i][j]
    for i in range(N)
    for j in range(M)
)+2)