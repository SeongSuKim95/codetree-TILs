from collections import deque

N,K,U,D = list(map(int,input().split()))

# N : map 크기
# K : K개의 도시 선택
# 이동 조건 : U <= 높이차 <= D

grid = [list(map(int,input().split())) for _ in range(N)]

positions = [
    (i,j)
    for i in range(N)
    for j in range(N)
    ]

selectedPos = []

dxs,dys = [-1,1,0,0], [0,0,-1,1]

answer = 0

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def bfs():

    q = deque()
    visited = [[False] * N for _ in range(N)]
    cityCnt = 0

    for sx,sy in selectedPos :
        q.append((sx,sy))
        visited[sx][sy] = True
        cityCnt += 1
    
    while q :
        cx, cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx, ny = cx+dx, cy+dy
            curHeight = grid[cx][cy]          
            if inRange(nx,ny):
                nextHeight = grid[nx][ny]
                diff = abs(curHeight-nextHeight)
                if not visited[nx][ny] and U<= diff and diff<=D: 
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    cityCnt += 1
    return cityCnt

def select(idx,cnt):
    global answer

    if cnt == K :
        answer = max(answer,bfs())
        return
    if idx == N*N:
        return
    
    select(idx+1,cnt)

    selectedPos.append(positions[idx])
    select(idx+1,cnt+1)
    selectedPos.pop()

select(0,0)
print(answer)