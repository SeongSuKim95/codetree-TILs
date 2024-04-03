N, M = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

dxs,dys = [-1,1,0,0],[0,0,-1,1]

visited = [
    [False] * M 
    for _ in range(N)
]

def inRange(x,y):

    return 0<=x<N and 0<=y<M

block = []
answer = 0

def choose(cx,cy,cnt):
    global answer

    if cnt == 3 :
        blockSum = 0
        for bx,by in block:
            blockSum += grid[bx][by]
        answer = max(answer,blockSum)
        return    
    
    for i in range(4):
        
        nx,ny = cx + dxs[i], cy + dys[i]
        
        if inRange(nx,ny) and not visited[nx][ny]:
            
            block.append((nx,ny))
            visited[nx][ny] = True
            choose(nx,ny,cnt+1)
            block.pop()
            visited[nx][ny] = False
            
            if cnt == 1:

                block.append((nx,ny))
                visited[nx][ny] = True
                choose(cx,cy,cnt+1)
                block.pop()
                visited[nx][ny] = False
    
for cx in range(N):
    for cy in range(M):
        block.append((cx,cy))
        visited[cx][cy] = True
        choose(cx,cy,0)
        block.pop()
        visited[cx][cy] = False

print(answer)