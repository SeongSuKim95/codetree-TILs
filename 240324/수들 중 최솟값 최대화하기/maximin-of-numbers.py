n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

visited = [False] * n
arr = []
answer = -1
def choose(idx):
    global answer
    if idx == n :
        minNumber = 1e9
        for i in range(n):
            minNumber = min(minNumber,grid[i][arr[i]])
        answer = max(answer,minNumber)
        return

    for i in range(n):
        if visited[i]:
            continue

        arr.append(i)
        visited[i]= True
        choose(idx+1)

        arr.pop()
        visited[i] = False

choose(0)
print(answer)