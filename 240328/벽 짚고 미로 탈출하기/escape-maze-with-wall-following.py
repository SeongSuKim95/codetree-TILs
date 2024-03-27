N = int(input())
cx,cy = list(map(lambda x : int(x) - 1 ,input().split()))

def str2num(x):

    if x == "#":
        return 1
    if x == ".":
        return 0

def printArr(arr):

    for row in arr:
        print(*row)

grid = [list(map(lambda x : str2num(x), input())) for _ in range(N)]

# 시작 위치에는 벽이 절대 주어지지 않고, (r+1,c)에는 항상 벽이 존재
# 우 하 좌 상
dxs,dys = [0, 1, 0, -1], [1, 0, -1, 0]
# 시작 : 우측
curDir = 0
cnt = 0
def inRange(x,y):

    return 0<=x<N and 0<=y<N

# 벽 1 , 빈 공간 0

def move(cx,cy):
    global cnt, curDir

    while True : 
        nx ,ny = cx + dxs[curDir], cy + dys[curDir]

        # 이동 가능
        if inRange(nx,ny):
            if grid[nx][ny] == 0 :
                
                wx, wy = nx + dxs[(curDir + 1 ) % 4], ny + dys[(curDir + 1) % 4]
                if grid[wx][wy]:
                    cx, cy = nx, ny
                    cnt += 1
                else :
                    cx, cy = wx, wy
                    cnt += 2
                    curDir = ( curDir + 1 ) % 4
            # 바라보고 있는 방향으로 이동하지 못할 경우
            elif grid[nx][ny] == 1 :
                curDir = ( curDir + 1 ) % 4
        else :
            cnt += 1
            break

move(cx,cy)
print(cnt)