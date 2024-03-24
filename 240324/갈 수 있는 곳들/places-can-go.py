from collections import deque

n, k = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]

starts = [tuple(map(lambda x : int(x)-1,input().split())) for _ in range(k)]

visited = [[False]*n for _ in range(n)]

def inRange(x,y):

    return 0<=x<n and 0<=y<n

def canGo(x,y):
    
    return not visited[x][y] and not grid[x][y]

def bfs():
    cnt = 0
    dxs,dys = [-1,1,0,0],[0,0,-1,1]

    q = deque()
    for sx,sy in starts:
        q.append((sx,sy))
        visited[sx][sy] = True
        cnt += 1
    while q :
        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cx+dx, cy+dy
            if inRange(nx,ny):
                if canGo(nx,ny):
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    cnt += 1
    return cnt

print(bfs())