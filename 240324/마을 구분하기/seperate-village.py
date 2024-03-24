N = int(input())

grid = [list(map(int,input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dxs,dys = [-1,1,0,0],[0,0,-1,1]

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def canGo(x,y):

    return not visited[x][y] and grid[x][y]

def printArr(arr):

    for row in arr:
        print(*row)
    print()

def dfs(cx,cy,color):

    for dx,dy in zip(dxs,dys):
        nx,ny = cx + dx, cy + dy
        if inRange(nx,ny):
            if canGo(nx,ny):
                visited[nx][ny] = True
                grid[nx][ny] = color
                dfs(nx,ny,color)
color = 1

for i in range(N):
    for j in range(N):
        if not visited[i][j] and grid[i][j]:
            grid[i][j] = color
            dfs(i,j,color)
            color += 1

colorCnt = {i:0 for i in range(1,color)}

for i in range(N):
    for j in range(N):
        if grid[i][j] :
            colorCnt[grid[i][j]] += 1
colorCnt = sorted(colorCnt.items(), key = lambda x : x[1])
print(color-1)
for key,value in colorCnt:
    print(value)