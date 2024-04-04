N = int(input())

# direction을 차곡차곡 쌓고 뒤에서 부터 순차적으로 1씩 감소

# 오른쪽 위쪽 왼쪽 아래쪽
dirs = [(0,1),(-1,0),(0,-1),(1,0)]

curves = [
    list(map(int,input().split()))
    for _ in range(N)
]

grid = [
    [0] * 100
    for _ in range(100)
]


def simulate():

    for x,y,d,g in curves:
        dirHistory = [d] 
        for _ in range(g):
            nextDirHistory = []
            for cd in dirHistory:
                nd = (cd + 1) % 4
                nextDirHistory.append(nd)
            dirHistory = dirHistory + nextDirHistory[::-1]
        
        cx,cy = x,y
        grid[cx][cy] = 1
        for cdir in dirHistory:
            cx,cy = cx + dirs[cdir][0], cy + dirs[cdir][1]
            grid[cx][cy] = 1

def isSquare(i,j):
    
    return (
        grid[i][j] and
        grid[i+1][j] and
        grid[i][j+1] and
        grid[i+1][j+1]
    )

def printArr(arr):

    for row in grid:
        print(*row[:10])
    print()


def countSquare():
    cnt = 0
    for i in range(99):
        for j in range(99):
            if isSquare(i,j):
                cnt += 1

    return cnt

simulate()

print(countSquare())