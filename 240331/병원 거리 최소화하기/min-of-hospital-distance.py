from collections import deque

# N X N 의 map
# M 개의 병원 남겨서 거리 최소화
# 병원과 사람 간의 거리 abs(x1-x2) + abs(y1-y2)

def printArr(arr):

    for row in arr:
        print(*row)
    print()

N,M = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

personList, hospitalList = [],[]

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 : # 사람인 경우
            personList.append((i,j))
        elif grid[i][j] == 2 : # 병원인 경우
            hospitalList.append((i,j))

hospitalNum = len(hospitalList)
selectedList = []
answer = 1e9

def inRange(x,y):
    
    return 0<=x<N and 0<=y<N

def getdist():
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    q = deque()
    visited = [
        [False] * N 
        for _ in range(N)
    ] 

    for idx in selectedList:
        hx,hy = hospitalList[idx]
        q.append((hx,hy))
        visited[hx][hy] = True

    dist = [
        [0] * N 
        for _ in range(N)
    ]
    # 병원에서 최단거리 구하기
    # 병원들의 위치에 대해선 visited 처리를 하면 안됨
    # 사람에 대해서만 visited 처리
    while q :
        chx,chy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx, ny = chx + dx, chy + dy
            if inRange(nx,ny):
                if not visited[nx][ny] and not dist[nx][ny] :
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[chx][chy] + 1
                    q.append((nx,ny))
    distSum = 0
    for px,py in personList:
        distSum += dist[px][py]
    
    return distSum

def choose(idx,cnt):
    global answer
    
    if cnt == M : 
        answer = min(answer,getdist())
        return
    
    if idx == hospitalNum :
        return 
    # 현재 idx 안 고름
    choose(idx+1,cnt)

    # 현재 idx 고름
    selectedList.append(idx)
    choose(idx+1,cnt+1)
    selectedList.pop()

choose(0,0)
print(answer)