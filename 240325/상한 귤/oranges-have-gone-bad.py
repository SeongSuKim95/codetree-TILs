from collections import deque

N, K = list(map(int,input().split()))
dxs,dys = [-1,1,0,0],[0,0,-1,1]

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

visited = [
    [False] * N
    for _ in range(N)
]

dist = [
    [0] * N 
    for _ in range(N)
]

starts = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 2 :
            starts.append((i,j))

def inRange(x,y):
    
    return 0<=x<N and 0<=y<N


def bfs():

    q = deque()
    for sx,sy in starts:
        q.append((sx,sy))
        visited[sx][sy] = True
    
    while q :
        
        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cx+dx, cy+dy
            if inRange(nx,ny):
                if not visited[nx][ny] and grid[nx][ny] :
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[cx][cy] + 1
                    q.append((nx,ny))

bfs()

for i in range(N):
    for j in range(N):
        if not dist[i][j] and not grid[i][j] :
            dist[i][j] = -1

for row in dist:
    print(*row)