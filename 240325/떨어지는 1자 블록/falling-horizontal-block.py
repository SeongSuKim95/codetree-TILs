N,M,K = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(N)]

K = K - 1

for i in range(N):
    flag = False
    for c in range(K,K+M):
        if grid[i][c] :
            flag = True
    if flag :
        targetRow = i - 1
        break

for i in range(K,K+M):
    grid[targetRow][i] = 1

for row in grid:
    print(*row)