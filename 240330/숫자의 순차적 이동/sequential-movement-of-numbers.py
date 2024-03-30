N, M = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

numPos = dict()
dxs,dys = [-1,-1,-1,0,1,1,1,0],[-1,0,1,1,1,0,-1,-1]

for i in range(N):
    for j in range(N):
        numPos[grid[i][j]] = (i,j)

def inRange(x,y):
    return 0<=x<N and 0<=y<N

def printArr(arr):

    for row in arr:
        print(*row)
    print()

def move():

    for num in range(1,N*N+1):
        cx,cy = numPos[num]
        curNum,maxNum = num,0
        destx,desty = 0,0
        for dx,dy in zip(dxs,dys):
            nx, ny = cx + dx,cy + dy
            if inRange(nx,ny):
                if grid[nx][ny] > maxNum : 
                    maxNum = max(maxNum,grid[nx][ny])
                    destx,desty = nx,ny
        grid[cx][cy],grid[destx][desty] = maxNum, curNum
        numPos[curNum],numPos[maxNum] = (destx,desty), (cx,cy)
for i in range(M):
    move()
printArr(grid)