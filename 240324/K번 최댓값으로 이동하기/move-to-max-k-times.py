from collections import deque

N, K = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(N)]

start = tuple(map(lambda x : int(x)-1,input().split()))

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def canGo(x,y,v):
    
    return not visited[x][y] and grid[x][y] < v

def bfs():
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    q = deque()
    sv,sx,sy = start
    minPos = (1,sx,sy)
    visited[sx][sy] = True
    q.append((sx,sy))
    while q :
        cur_x,cur_y = q.popleft()   
        for dx,dy in zip(dxs,dys):
            nx,ny = cur_x+dx,cur_y+dy
            if inRange(nx,ny):
                if canGo(nx,ny,sv):
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    minPos = min(minPos,(-grid[nx][ny],nx,ny))
                    
    return (-minPos[0],minPos[1],minPos[2])
sx,sy = start
start = (grid[sx][sy],sx,sy)
for _ in range(K):
    visited = [[False] * N for _ in range(N)]
    start = bfs()

print(start[1]+1,start[2]+1)