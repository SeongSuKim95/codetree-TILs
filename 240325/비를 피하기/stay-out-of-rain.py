from collections import deque

# N : 맵 크기
# H : 사람의 수
# M : 비를 피할 수 있는 공간의 수
N,H,M = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(N)]

# 입력 : 
# 0 --> 이동할 수 있는 공간
# 1 --> 벽이 있는 공간 (이동 불가)
# 2 --> 사람이 서있는 공간 (출발점)
# 3 --> 비를 피할 수 있는 공간

# 출력 :
# 사람이 있던 칸 : 최단거리 출력, 못피하면 -1
# 사람이 없던 칸 : 0

# 비를 피할 수 있는 공간을 시작점으로, 사람이 있는 공간까지의 최단거리 구하기
starts = []
visited = [[False] * N for _ in range(N)]
dxs,dys = [-1,1,0,0],[0,0,-1,1]
dist = [[0]* N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if grid[i][j] == 3 :
            starts.append((i,j))

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def bfs():

    q = deque()
    
    for sx,sy in starts:
        q.append((sx,sy))
        visited[sx][sy] == True
    
    while q :
        cx,cy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = cx+dx, cy+dy
            if inRange(nx,ny):
                if not visited[nx][ny] and grid[nx][ny] != 1 and not dist[nx][ny]: 
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[cx][cy] + 1
                    q.append((nx,ny))    
def printArr(arr):

    for row in arr:
        print(*row)

bfs()

answer = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if grid[i][j] == 2 :
            if dist[i][j] :
                answer[i][j] = dist[i][j]
            else :
                answer[i][j] = -1
printArr(answer)