from collections import deque

N, L, R  = list(map(int,input().split()))
EMPTY = 0

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]

dxs,dys = [-1,1,0,0],[0,0,-1,1]

def printArr(arr):

    for row in arr:
        print(*row)
    print()

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def canMerge(pos1,pos2):
    cx,cy = pos1
    nx,ny = pos2
    if L <= abs(grid[nx][ny] - grid[cx][cy]) <= R:
        return True
    return False

def isSame(arr1,arr2):

    for i in range(N):
        for j in range(N):
            if arr1[i][j] != arr2[i][j]:
                return False
    return True

def simulate():

    clusterGrid = [
        [EMPTY] * N 
        for _ in range(N)
    ]

    clusterIdx = 0
    for i in range(N):
        for j in range(N):
            if clusterGrid[i][j] == EMPTY:
                clusterIdx += 1
                clusterGrid[i][j] = clusterIdx
                q = deque([(i,j)])
                while q :
                    cx,cy = q.popleft()
                    for dx,dy in zip(dxs,dys):
                        nx,ny = cx+dx, cy+dy
                        if inRange(nx,ny):
                            if not clusterGrid[nx][ny] and canMerge((cx,cy),(nx,ny)):
                                clusterGrid[nx][ny] = clusterIdx
                                q.append((nx,ny))

    clusters = [
        [] for i in range(clusterIdx+1)
    ]

    for i in range(N):
        for j in range(N):
            clusters[clusterGrid[i][j]].append(grid[i][j])
    
    for idx, cluster in enumerate(clusters):
        if idx == 0 :
            continue
        clusters[idx] = sum(cluster) // len(cluster)

    for i in range(N):
        for j in range(N):
            grid[i][j] = clusters[clusterGrid[i][j]]

elapsedTime = 0
while True :
    curGrid = [
        row[:] for row in grid
    ]
    simulate()
    elapsedTime += 1

    nextGrid = [
        row[:] for row in grid  
    ]
    if isSame(curGrid,nextGrid):
        break

print(elapsedTime-1)