N = int(input())

grid = [list(map(int,input().split())) for _ in range(N)]
positions = []
Bombs = []
answer = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] : 
            positions.append((i,j))
bombCnt = len(positions)

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def explosion(arr):

    gridTmp = [[0]*N for _ in range(N)]
    cnt = 0
    # 1, 2, 3
    explosionRange = {
        1 : [(0,0),(-1,0),(-2,0),(1,0),(2,0)],
        2 : [(0,0),(-1,0),(1,0),(0,-1),(0,1)],
        3 : [(0,0),(-1,-1),(-1,1),(1,1),(1,-1)]
    }

    for (pos_x,pos_y),bomb in zip(positions,Bombs):
        for dx,dy in explosionRange[bomb]:
            cur_x,cur_y = pos_x + dx, pos_y + dy
            if inRange(cur_x,cur_y):
                gridTmp[cur_x][cur_y] = 1

    for i in range(N):
        for j in range(N):
            if gridTmp[i][j]:
                cnt += 1
    return cnt

def getBomb(idx):
    global answer
    if idx == bombCnt :
        answer = max(answer,explosion(Bombs))
        return 
    
    for i in range(1,4):
        Bombs.append(i)
        getBomb(idx+1)
        Bombs.pop()

getBomb(0)
print(answer)