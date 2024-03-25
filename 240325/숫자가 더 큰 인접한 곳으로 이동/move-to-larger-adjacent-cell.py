N, r, c = list(map(int,input().split()))

cx, cy = r - 1, c - 1

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def inRange(x,y):

    return 0<=x<N and 0<=y<N

answer = []

while True : 
    cxTmp,cyTmp = cx,cy
    answer.append(grid[cx][cy])
    for dx,dy in zip(dxs,dys):
        nx,ny = cx+dx, cy+dy
        if inRange(nx,ny):
            if grid[cx][cy] < grid[nx][ny]:
                cx,cy = nx,ny
                break
    if cxTmp == cx and cyTmp == cy:
        break

print(*answer)