# 격자 크기, 원자 개수, 시간 초
N,M,K = list(map(int,input().split())) 

grid = [
    [[] for _ in range(N)]
    for _ in range(N)
]

# x,y,m,s,d
# 좌표, 질량, 속력, 방향
atoms = [
    list(map(int,input().split()))
    for _ in range(M)
]
# index
# 0 2 4 6 짝수 --> 상하좌우
# 1 3 5 7 홀수 --> 대각
dirs = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

for x,y,m,s,d in atoms:
    x,y = x-1,y-1
    grid[x][y].append((m,s,d))

def move():

    nextGrid = [
        [[] for _ in range(N)]
        for _ in range(N)
    ]

    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                cx,cy = i,j
                curAtoms = grid[cx][cy][:]
                for cm,cs,cd in curAtoms:
                    nx,ny = (cx + cs * dirs[cd][0]) % N , (cy + cs * dirs[cd][1]) % N
                    nextGrid[nx][ny].append((cm,cs,cd))
    
    for i in range(N):
        for j in range(N):
            grid[i][j] = nextGrid[i][j][:]

def mergeAndSplit():

    nextGrid = [
        [[] for _ in range(N)]
        for _ in range(N)
    ]

    for i in range(N):
        for j in range(N):
            if grid[i][j] and len(grid[i][j]) >= 2 :
                curAtoms = grid[i][j]
                weightSum , velocitySum, directionSum, atomNum = 0, 0, 0, len(curAtoms)
                for cm,cs,cd in curAtoms:
                    weightSum += cm
                    velocitySum += cs
                    directionSum += cd % 2 # 짝수 : 상하좌우 , 홀수 : 대각
                nextWeight,nextVelocity = weightSum // 5, velocitySum // atomNum
                # 질량이 0이면 소멸
                if nextWeight == 0 :
                    continue
                # 방향이 전부 상하좌우이거나 대각인 경우
                if directionSum == 0 or directionSum == atomNum:
                    nextDirections = [0,2,4,6]
                else : # 그렇지 않은 경우
                    nextDirections = [1,3,5,7]

                for nextDir in nextDirections :
                    nextGrid[i][j].append((nextWeight,nextVelocity,nextDir))
            else :
                nextGrid[i][j] = grid[i][j][:]
    for i in range(N):
        for j in range(N):
            grid[i][j] = nextGrid[i][j][:]

def printArr(arr):
    for row in arr:
        print(*row)
    print()

for _ in range(K):
    move()

    mergeAndSplit()


answer = 0 
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            for cm,_,_ in grid[i][j]:
                answer += cm

print(answer)