from collections import deque

N = int(input())

sx,sy,ex,ey = list(map(lambda x : int(x) - 1,input().split()))

dxs,dys = [-2,-1,1,2,2,1,-1,-2],[1,2,2,1,-1,-2,-2,-1]

visited = [[False] * N for _ in range(N)]

grid = [[0]* N for _ in range(N)]

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def bfs():
    visited[sx][sy] = True
    q = deque([(sx,sy)])
    while q :
        cx, cy = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = cx + dx, cy+ dy
            if inRange(nx,ny):
                if not visited[nx][ny] :
                    visited[nx][ny] = True
                    grid[nx][ny] = grid[cx][cy] + 1
                    if (nx,ny) == (ex,ey):
                        return True
                    q.append((nx,ny))
    return False

def printArr(arr):

    for row in arr:
        print(*row)

if bfs():
    print(grid[ex][ey])
else:
    print(-1)