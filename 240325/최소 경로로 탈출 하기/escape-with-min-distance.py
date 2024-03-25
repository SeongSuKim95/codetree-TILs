from collections import deque

N, M = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(N)]

dxs,dys = [-1,1,0,0],[0,0,-1,1]
visited = [[False] * M for _ in range(N)]

def inRange(x,y):
    
    return 0<=x<N and 0<=y<M

def bfs():

    q = deque([(0,0)])
    visited[0][0] = True
    while q: 
        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cx+dx, cy+dy
            if inRange(nx,ny):
                if not visited[nx][ny] and grid[nx][ny]:
                    visited[nx][ny] = True
                    grid[nx][ny] = grid[cx][cy] + 1
                    q.append((nx,ny))

bfs()
if visited[N-1][M-1]:
    print(grid[N-1][M-1]-1)
else :
    print(-1)