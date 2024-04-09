from collections import deque

N = int(input())

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

dxs,dys = [-1,1,0,0],[0,0,-1,1]
scale = N // 2 
answer = 0
def printArr(arr):

    for row in arr:
        print(*row)
    print()

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def getScore():

    q = deque()

    visited = [
        [0] * N 
        for _ in range(N)
    ]

    coloredMap = [
        [0] * N 
        for _ in range(N)
    ]
    
    colordict = {
        i : [] for i in range(1,11)
    }
    
    color = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:

                q.append((i,j))
                visited[i][j] = 1
                color += 1
                coloredMap[i][j] = color
                colordict[color].append((i,j))
                cnum = grid[i][j]
            
                while q :
                    cx,cy = q.popleft()   
                    for dx,dy in zip(dxs,dys):
                        nx,ny = cx + dx, cy + dy
                        if inRange(nx,ny) and not visited[nx][ny] and grid[nx][ny] == cnum:
                            q.append((nx,ny))
                            coloredMap[nx][ny] = color
                            colordict[color].append((nx,ny))
                            visited[nx][ny] = 1
    pairScores = []

    for color1, poslist1 in colordict.items():
        for color2, poslist2 in colordict.items():
            if color1 < color2 and poslist1 and poslist2:
                
                numEdges = 0 
                num1, num2 = grid[poslist1[0][0]][poslist1[0][1]], grid[poslist2[0][0]][poslist2[0][1]]
                
                for px1,py1 in poslist1:
                    
                    for dx,dy in zip(dxs,dys):
                        nx,ny = px1+dx,py1+dy
                        if inRange(nx,ny) and coloredMap[nx][ny] == color2:
                           numEdges += 1

                pairScore = (len(poslist1) + len(poslist2)) * num1 * num2 * numEdges
                pairScores.append(pairScore)
    
    return sum(pairScores)

def centerRotate():

    nextGrid = [
        [0] * N
        for _ in range(N)
    ]

    for i in range(N):
        for j in range(N):
            if i == N // 2 or j == N // 2:
                nextGrid[i][j] = grid[j][N-1-i]
            else :
                nextGrid[i][j] = grid[i][j]
    
    for i in range(N):
        for j in range(N):
            grid[i][j] = nextGrid[i][j]

def rotateOneCorner(cx,cy):

    nextSmallGrid = [
        [0] * scale
        for _ in range(scale)
    ]

    curSmallGrid = [
        [grid[i][j] for j in range(cy,cy+scale)]
        for i in range(cx,cx+scale)
    ]
    
    for i in range(scale):
        for j in range(scale):
            nextSmallGrid[i][j] = curSmallGrid[scale-1-j][i]

    for i in range(scale):
        for j in range(scale):
            grid[cx+i][cy+j] = nextSmallGrid[i][j]

def cornerRotate():
    
    rotateOneCorner(0,0)
    rotateOneCorner(scale+1,0)
    rotateOneCorner(0,scale+1)
    rotateOneCorner(scale+1,scale+1)

def rotate():

    centerRotate()
    cornerRotate()

answer = getScore()
for _ in range(3):
    rotate()
    answer += getScore()

print(answer)