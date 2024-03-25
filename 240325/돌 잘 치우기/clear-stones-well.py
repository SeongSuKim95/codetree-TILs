from collections import deque

n, k, m = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]
# 1 : rock
starts = [tuple(map(lambda x : int(x) - 1,input().split())) for _ in range(k)]

rockPos = []

answer = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] :
            rockPos.append((i,j))

# 치울 돌 m개 선택 하기
mRocks = []

def inRange(x,y):

    return 0<=x<n and 0<=y<n

def bfs(rocks):
    gridTemp = [row[:] for row in grid]
    visited = [[False] * n for _ in range(n)]
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    cnt = 0
    for rx,ry in rocks:
        gridTemp[rx][ry] = 0
    
    q = deque()
    for sx,sy in starts:
        q.append((sx,sy))
        visited[sx][sy] = True
        cnt += 1
    while q :
        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cx+dx,cy+dy
            if inRange(nx,ny):
                if not visited[nx][ny] and not gridTemp[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    cnt += 1
    return cnt

def choose(idx,cnt):
    global answer

    if idx == len(rockPos):
        return
        
    if cnt == m :
        regionCnt = bfs(mRocks)
        answer = max(answer,regionCnt)
        return


    choose(idx+1,cnt)

    mRocks.append(rockPos[idx])
    choose(idx+1,cnt+1)
    mRocks.pop()


choose(0,0)
print(answer)