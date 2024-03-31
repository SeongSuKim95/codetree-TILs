# N : 격자 크기, M: 구슬 개수 , t : 경과 시간, k : 최대 충돌 가능 개수 
N,M,t,k = list(map(int,input().split()))

def printArr(arr):

    for row in arr:
        print(*row)
    print()

def inRange(x,y):

    return 0<=x<N and 0<=y<N

# 구슬 번호는 입력 받는 순서대로
# r,c,d,v
# d : U,D,R,L
# v : 1초에 v 칸 이동
# v,num,dir
# 0 : U
# 1 : R
# 2 : D
# 3 : L
dxs,dys = [-1,0,1,0],[0,1,0,-1]
def convertInput(input):
    dirMap = {
        "U" : 0 , # (-1,0)
        "R" : 1 , # (0,1),
        "D" : 2 , # (1,0),
        "L" : 3 , # (0,-1)
    }
    if input.isalpha():
        return dirMap[input] 
    return int(input)

grid = [
    [[] for _ in range(N)]
    for _ in range(N)
]

for i in range(1,M+1):
    r,c,dir,v = list(map(convertInput,input().split()))
    r,c = r-1, c-1
    grid[r][c].append((v,i,dir))

def move():

    nextGrid = [
        [[] for _ in range(N)]
        for _ in range(N)
    ]

    for cx in range(N):
        for cy in range(N):
            curx,cury = cx,cy
            if grid[cx][cy] != []:               
                for cv,cnum,cdir in grid[cx][cy]:
                    # 현재 공 이동
                    for _ in range(cv):
                        cdx, cdy = dxs[cdir], dys[cdir]
                        nx,ny = curx + cdx, cury + cdy
                        if inRange(nx,ny):
                            curx,cury = nx,ny
                        else:
                            cdir = (cdir+2) % 4
                            cdx,cdy = dxs[cdir], dys[cdir]
                            curx,cury = curx + cdx, cury + cdy
                    
                    # 도착점을 nextGrid 에 기록
                    nextGrid[curx][cury].append((cv,cnum,cdir))
      
    for i in range(N):
        for j in range(N):
            nextList = nextGrid[i][j][:]
            if len(nextList) <= k : 
                grid[i][j] = nextGrid[i][j][:]
            else :
                nextList = sorted(nextList,key = lambda x : (-x[0],-x[1]))
                grid[i][j] = nextList[:k][:]
    
# printArr(grid)
for _ in range(t):
    move()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(grid[i][j])

print(answer)