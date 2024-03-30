T = int(input())
EMPTY = 5

def printArr(arr):

    for row in arr:
        print(*row)
    print()

dirMap = {
    "U" : 0,
    "R" : 1,
    "D" : 2,
    "L" : 3 
}

# 상 우 하 좌 --> 2 씩 더하면 반대 방향으로 뒤집힘
dirs = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
]

def printArr(arr):

    for row in arr:
        print(*row)
    print()

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def isDuplicate(arr1,arr2):

    for i in range(N):
        for j in range(N):
            if arr1[i][j] != arr2[i][j] :
                return False
    return True

def simulate():
    gridHistory = []

    while True :
        # printArr(grid)
        nextGrid = [[[] for _ in range(N)] for _ in range(N)]
        for cx in range(N):
            for cy in range(N):
                if grid[cx][cy] != EMPTY : # 이동
                    cdir = grid[cx][cy]
                    dx,dy = dirs[cdir][0], dirs[cdir][1]
                    nx,ny = cx + dx, cy + dy
                    if inRange(nx,ny):
                        nextGrid[nx][ny].append(cdir)
                    else :
                        nextGrid[cx][cy].append((cdir+2)%len(dirs)) # 반대 방향으로 바꾸기        
        for i in range(N):
            for j in range(N):
                if len(nextGrid[i][j]) == 1 : 
                    grid[i][j] = nextGrid[i][j][0]
                elif len(nextGrid[i][j]) == 0 :
                    grid[i][j] = EMPTY
                else :
                    grid[i][j] = EMPTY
        curGrid = [
            row[:] for row in grid
        ]
        if len(gridHistory) < 2 * N:
            gridHistory.append(curGrid)
        else :
            isValid = isDuplicate(gridHistory[0],curGrid)
            if isValid : 
                break
            else :
                gridHistory = gridHistory[1:]
                gridHistory.append(curGrid)
def printNumballs():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] != EMPTY :
                cnt += 1
    return cnt

for _ in range(T):

    N, M = list(map(int,input().split()))
    
    balls = [list(map(lambda x : dirMap[x] if x.isalpha() else int(x)-1,input().split())) for _ in range(M)]
    
    grid = [[EMPTY for _ in range(N)] for _ in range(N)]
    
    for x,y,dir in balls:
        grid[x][y] = dir
    simulate()
    print(printNumballs())