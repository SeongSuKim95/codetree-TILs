from collections import deque

N, M = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(N)]

dxs,dys = [-1,1,0,0],[0,0,-1,1]
meltedCnt = 0
def inRange(x,y):

    return 0<=x<N and 0<=y<M

def bfs():
    global meltedCnt

    visited = [[False]*M for _ in range(N)]
    gridNext = [row[:] for row in grid]

    q = deque([(0,0)])
    visited[0][0] = True
    cnt = 1

    while q :

        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cx+dx,cy+dy
            if inRange(nx,ny):
                if not visited[nx][ny] and grid[nx][ny] == 0 :
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    cnt += 1
    if cnt == M*N :
        return True

    meltedCnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] :
                for dx,dy in zip(dxs,dys):
                    nx,ny = i+dx,j+dy
                    if inRange(nx,ny):
                        if gridNext[nx][ny]:
                            gridNext[nx][ny] = 0
                            meltedCnt += 1
    
    for i in range(N):
        for j in range(M):
            grid[i][j] = gridNext[i][j]
    
    return False

t = 0
while True:
    melted = bfs()
    if melted:
        break
    t += 1

print(t,meltedCnt)