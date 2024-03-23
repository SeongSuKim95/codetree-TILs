n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

arr = []
visited = [False] * n
answer = 0

def choose(idx):
    global answer
    if idx == n :
        _sum = 0
        for i in range(n):
            _sum += grid[i][arr[i]]
        answer = max(answer,_sum)
        return

    for i in range(n):
        if visited[i]:
            continue
        arr.append(i)
        visited[i] = True

        choose(idx+1)
        
        arr.pop()
        visited[i] = False

choose(0)
print(answer)