N = int(input())

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

answer = 0
# 1 : /, 2 : \
# 상 하 좌 우
# 0  1 2 3 
dxs, dys = [-1,1,0,0],[0,0,-1,1]

# 1 : /            2 : \
# 하(1) -> 좌(2)    하(1) -> 우(3)
# 우(3) -> 상(0)    우(3) -> 하(1)
# 좌(2) -> 하(1)    좌(2) -> 상(0)
# 상(0) -> 우(3)    상(0) -> 좌(2)

def changeDir(curDir, slope):
    slope1 = {
        1 : 2, 
        3 : 0,
        2 : 1,
        0 : 3
    }
    slope2 = {
        1 : 3,
        3 : 1,
        2 : 0,
        0 : 2
    }
    if slope == 1 :
        return slope1[curDir]
    if slope == 2 :
        return slope2[curDir]

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def move(cx,cy,cdir):
    elapsedTime = 1
    while inRange(cx,cy):
        if grid[cx][cy] == 0 :
            cx, cy = cx + dxs[cdir], cy + dys[cdir]
            elapsedTime += 1
            continue
        if grid[cx][cy] == 1 :
            cdir = changeDir(cdir,1)
            cx, cy = cx + dxs[cdir], cy + dys[cdir]
            elapsedTime += 1
            continue
        if grid[cx][cy] == 2 :
            cdir = changeDir(cdir,2)
            cx, cy = cx + dxs[cdir], cy + dys[cdir]
            elapsedTime += 1
            continue

    return elapsedTime 

def simulate():
    global answer
    # 상 하 좌 우
    # 0  1 2 3 
    for i in range(N):
        answer = max(answer,move(i,0,3)) # 우향 진행
    for j in range(N):
        answer = max(answer,move(0,j,1)) # 하향 진행 
    for i in range(N):
        answer = max(answer,move(i,N-1,2)) # 좌향 진행 
    for j in range(N):
        answer = max(answer,move(N-1,j,0)) # 상향 진행

simulate()
print(answer)