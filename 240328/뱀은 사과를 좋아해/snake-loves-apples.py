N, M, K = list(map(int,input().split()))

dirs = {
    'R' : (0,1),
    'U' : (-1,0),
    'D' : (1,0),
    'L' : (0,-1)
}

grid = [[0] * N for _ in range(N)]

apples = [
    tuple(map(lambda x : int(x)-1, input().split()))
    for _ in range(M)
]

for ax,ay in apples:
    grid[ax][ay] = 2


moves = [
     tuple(map(lambda x : x if x.isalpha() else int(x),input().split()))
     for _ in range(K)
]

def inRange(x,y):

    return 0<=x<N and 0<=y<N

# 몸통을 list로 관리?
def solve():
    cx,cy = 0,0
    length = 1
    history = [(0,0)]
    elapsedTime = 0
    for curDir, curTime in moves:
        for t in range(curTime):
            nx, ny = cx + dirs[curDir][0] , cy + dirs[curDir][1]
            elapsedTime += 1
            if not inRange(nx,ny): # 부딪혔을때 조건 추가해야함
                return(elapsedTime)
            if grid[nx][ny] == 2 :
                length += 1
                grid[nx][ny] = 0
            if (nx,ny) in history[:length-1]:
                return(elapsedTime)
            history = [(nx,ny)] + history[:length-1]
            cx,cy = nx,ny
    return elapsedTime

print(solve())