N, M = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

numPos = dict()
dxs, dys = [-1,1,0,0,-1,-1,1,1],[0,0,-1,1,-1,1,-1,1]

def inRange(x,y):
    return 0<=x<N and 0<=y<N

def printArr(arr):

    for row in arr:
        print(*row)
    print()

for i in range(N):
    for j in range(N):
        numPos[grid[i][j]] = (i,j)

def move():
    
    # nextGrid = [
    #     [0] * N for _ in range(N)
    # ]

    # 인접한 칸들 중 가장 큰 숫자와 가운데 숫자를 교환

    for num in range(1, N*N+1):
        cx, cy = numPos[num]
        destx,desty = 0,0
        for dx,dy in zip(dxs,dys):
            nx,ny = cx + dx, cy+ dy
            maxNum = 0
            if inRange(nx,ny):
                if grid[nx][ny] > maxNum : 
                    maxNum = max(grid[nx][ny], maxNum)
                    destx,desty = nx,ny
        curNum,destNum = grid[destx][desty],grid[cx][cy]
        grid[destx][desty],grid[cx][cy] = destNum, curNum         
        printArr(grid)
        
move()