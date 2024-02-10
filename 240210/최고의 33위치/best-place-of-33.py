N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

answer = -1
for i in range(N-2):
    for j in range(N-2):
        sum = 0
        for x in range(i,i+3):
            for y in range(j,j+3):
                sum += grid[x][y]
        answer = max(answer,sum)

print(answer)