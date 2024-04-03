from collections import deque

N, M = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

answer = 0

def canGo(x,y):

    return not grid[x][y]

def inRange(x,y):

    return 0<=x<N and 0<=y<M


def bfs():

    visited = [
        [False] * M
        for _ in range(N)
    ]
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 :
                visited[i][j] = True

    q = deque()
    for fx,fy in Fires:
        q.append((fx,fy))
        visited[fx][fy] = True
    dxs,dys = [-1,1,0,0],[0,0,-1,1]

    while q: 
        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cx+dx,cy+dy
            if inRange(nx,ny) and not visited[nx][ny] and canGo(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny))
    cnt = 0 
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                cnt += 1
    
    return cnt

def printArr(arr):

    for row in arr:
        print(*row)
    print()

# 2:불, 1:방화벽, 0:빈 칸
Emptys = []
Fires = []
for i in range(N):
    for j in range(M):
        if not grid[i][j]:
           Emptys.append((i,j))
        if grid[i][j] == 2 :
           Fires.append((i,j))

def choose(idx,cnt):
    global answer

    if cnt == 3 :
        answer = max(answer,bfs())
        return

    if idx == len(Emptys):
        return
    
    grid[Emptys[idx][0]][Emptys[idx][1]] = 1
    choose(idx+1,cnt+1)
    grid[Emptys[idx][0]][Emptys[idx][1]] = 0

    choose(idx+1,cnt)


choose(0,0)
print(answer)