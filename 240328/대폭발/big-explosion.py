n,m,r,c = list(map(int,input().split()))
# m초가 되었을 떄 
r,c = r-1, c-1

grid = [[0] * n for _ in range(n)]

grid[r][c] = 1

dxs,dys = [-1,1,0,0],[0,0,-1,1]

def inRange(x,y):

    return 0<=x<n and 0<=y<n

def printArr(arr):

    for row in arr:
        print(*row)

def createBombs():

    curBombs = [(r,c)]
    for t in range(m):
        newBombs = []
        for bx,by in curBombs :
            for dx,dy in zip(dxs,dys):
                nx, ny = bx + dx * (2**t), by + dy * (2**t)
                if inRange(nx,ny):
                    grid[nx][ny] = 1
                    newBombs.append((nx,ny))
        curBombs += newBombs[:]
    # printArr(grid)

def countBombs():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                cnt += 1
    return cnt

createBombs()
print(countBombs())