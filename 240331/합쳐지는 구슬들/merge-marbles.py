N,M,T = list(map(int,input().split()))

def changeInput(inputList):
    r,c,dir,w,num = inputList
    dirs = {
        "U" : 0,
        "R" : 1,
        "D" : 2,
        "L" : 3,
    }

    return (r-1,c-1,num,w,dirs[dir])

dxs,dys = [-1,0,1,0],[0,1,0,-1]

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def printArr(arr):

    for row in arr:
        print(*row)

grid = [
    [[] for _ in range(N)]
    for _ in range(N)
]

balls = [
    changeInput(list(map(lambda x : x if x.isalpha() else int(x),input().split()))+[i])
    for i in range(1,M+1)
]

for x,y,num,w,dir in balls:
    grid[x][y].append((num,w,dir))

def move():
    nextGrid = [
        [[] for _ in range(N)]
        for _ in range(N)
    ]

    for cx in range(N):
        for cy in range(N):
            if grid[cx][cy] : 
                cnum,cw,cdir = grid[cx][cy][0]
                nx,ny = cx + dxs[cdir],cy + dys[cdir]
                if inRange(nx,ny): # 범위 내에 있는 경우
                    nextGrid[nx][ny].append((cnum,cw,cdir))
                else :
                    nextGrid[cx][cy].append((cnum,cw,(cdir+2) % 4))
    # 충돌 처리
    for cx in range(N):
        for cy in range(N):
            if len(nextGrid[cx][cy]) > 1 : # 한개 이상인 경우
                curList = sorted(nextGrid[cx][cy],reverse = True)
                maxNum , _ , maxNumDir = curList[0]
                weightSum = 0
                for _,cw,_ in curList : 
                    weightSum += cw

                nextGrid[cx][cy] = [(maxNum,weightSum,maxNumDir)]
    
    # nextGrid -> grid 에 옮기기
    for i in range(N):
        for j in range(N):
            grid[i][j] = nextGrid[i][j]

for _ in range(T):
    move()

maxWeight, cnt = 0,0

for i in range(N):
    for j in range(N):
        if grid[i][j] :
            maxWeight = max(maxWeight,grid[i][j][0][1])
            cnt += 1

print(cnt,maxWeight)