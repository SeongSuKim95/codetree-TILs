n, m, t = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]

balls = [
    tuple(map(lambda x : int(x)-1,input().split()))
    for _ in range(m)
]
count = [[0]* n for _ in range(n)]
for bx,by in balls:
    count[bx][by] += 1

dxs, dys = [0,0,1,-1],[1,-1,0,0]

def inRange(x,y):

    return 0<=x<n and 0<=y<n

def printArr(arr):

    for row in arr:
        print(*row)
    print()
    
def simulate():
    for _ in range(t):
        nextCount = [
            [0] * n
            for _ in range(n)
        ]
        
        for i in range(n):
            for j in range(n):
                if count[i][j] :
                    curNum = 0
                    nextx,nexty = 0,0
                    for dx,dy in zip(dxs,dys):
                        nx,ny = i + dx, j + dy
                        if inRange(nx,ny):
                            if grid[nx][ny] > curNum : 
                                curNum = grid[nx][ny]
                                nextx,nexty = nx,ny
                    nextCount[nextx][nexty] += 1

        for i in range(n):
            for j in range(n):
                if nextCount[i][j] > 1 :
                    count[i][j] = 0 
                else :
                    count[i][j] = nextCount[i][j]
simulate()
cnt = 0

for i in range(n):
    for j in range(n):
        if count[i][j] :
            cnt += 1
print(cnt)