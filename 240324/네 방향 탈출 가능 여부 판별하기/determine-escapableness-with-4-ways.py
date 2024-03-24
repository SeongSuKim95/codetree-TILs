from collections import deque

N,M = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dxs,dys = [-1,1,0,0],[0,0,-1,1]

def inRange(x,y):

    return 0<=x<N and 0<=y<M

def canGo(x,y):

    return not visited[x][y] and grid[x][y]

def bfs(x,y):

    q = deque([(x,y)])
    visited[x][y] = True
    while q :
        cur_x,cur_y = q.popleft()
        visited[cur_x][cur_y] = True
        for dx,dy in zip(dxs,dys):
            nx,ny = cur_x+dx,cur_y+dy
            if inRange(nx,ny):
                if canGo(nx,ny):
                    q.append((nx,ny))

bfs(0,0)

print(int(visited[N-1][M-1]))