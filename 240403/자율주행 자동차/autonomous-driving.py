N,M = list(map(int,input().split()))

# 북 동 남 서
dxs, dys = [-1,0,1,0],[0,1,0,-1]

cx,cy,cdir = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

visited = [
    [False] * M
    for _ in range(N)
]


def canGo(x,y):

    return not visited[x][y] and not grid[x][y]

def simulate():

    global cx,cy,cdir,answer
        
    for i in range(1,5):
        ndir = (cdir - i) % 4
        ndx,ndy = dxs[ndir],dys[ndir]
        nx,ny = cx + ndx, cy + ndy
        if canGo(nx,ny):
            visited[nx][ny] = True
            answer += 1
            cdir,cx,cy = ndir,nx,ny
            return True

    dx,dy = dxs[cdir],dys[cdir]
    nx,ny = cx - dx, cy - dy
    
    if canGo(nx,ny):
        visited[nx][ny] = True
        answer += 1
        cx,cy = nx,ny 
        return True
        
    return False

visited[cx][cy] = True
answer = 1
while True :
    if not simulate():
        break

print(answer)