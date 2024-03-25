from collections import deque
# N : 격자 크기
# K : 없애야 할 벽의 개수

N, K = list(map(int,input().split()))


# 0 : 이동 가능
# 1 : 벽 있어서 이동 불가

grid = [list(map(int,input().split())) for _ in range(N)]

sx, sy = list(map(lambda x : int(x) - 1,input().split()))
ex, ey = list(map(lambda x : int(x) - 1,input().split()))

walls = []
selectedWalls = []
dxs,dys = [-1,1,0,0],[0,0,-1,1]
answer = 1e9

for i in range(N):
    for j in range(N):
        if grid[i][j] : 
            walls.append((i,j))

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def bfs(arr):
    visited = [[False] * N for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    q = deque([(sx,sy)])
    visited[sx][sy] = True
    while q : 
        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cx+dx, cy+dy
            if inRange(nx,ny):
                if not visited[nx][ny] and arr[nx][ny] == 0:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[cx][cy] + 1
                    q.append((nx,ny))
    
    return dist[ex][ey]

def choose(idx,cnt):
    global answer
    
    if cnt == K :
        gridTemp = [row[:] for row in grid]
        for sx,sy in selectedWalls :
            gridTemp[sx][sy] = 0
        minDist = bfs(gridTemp)
        if minDist == 0 :
            pass
        else :
            answer = min(answer,minDist)
        return
    
    if idx == len(walls):
        return
    
    choose(idx+1,cnt)

    selectedWalls.append(walls[idx])
    choose(idx+1,cnt+1)
    selectedWalls.pop()

choose(0,0)

if answer == 1e9:
    print(-1)
else:
    print(answer)