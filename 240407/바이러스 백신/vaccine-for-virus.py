from collections import deque

# N X N , M 개의 병원 고르기
N, M = list(map(int,input().split()))

# 0 : 바이러스
# 1 : 벽
# 2 : 병원
 
VIRUS = 0
WALL = 1
HOSPITAL = 2

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

answer = 1e9
hospitalList = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == HOSPITAL:
            hospitalList.append((i,j))

selectedList = []

def printArr(arr):

    for row in arr:
        print(*row)
    print()

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def bfs():

    
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    
    # 병원 값은 1로, 나중에 결과 값에서 1빼주기
    steps = [
        [0] * N
        for _ in range(N)
    ]

    q = deque()
    
    for hidx in selectedList:
        hx,hy = hospitalList[hidx]
        q.append((hx,hy))
        steps[hx][hy] = 1
    
    maxStep = 0

    while q: 
        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cx+dx,cy+dy
            if inRange(nx,ny) and steps[nx][ny] == 0 and grid[nx][ny] != WALL:
                q.append((nx,ny))
                steps[nx][ny] = steps[cx][cy] + 1
                if grid[nx][ny] == VIRUS:
                    maxStep = max(maxStep, steps[nx][ny])
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == VIRUS :
                if steps[i][j] == 0 :
                    return -1
    return maxStep - 1 

    

def choose(idx,cnt):
    global answer

    if cnt == M :
        answer = min(answer,bfs())
        return 

    if idx == len(hospitalList):
        
        return

    selectedList.append(idx)
    choose(idx+1,cnt+1)
    selectedList.pop()

    choose(idx+1,cnt)
    

choose(0,0)
print(answer)