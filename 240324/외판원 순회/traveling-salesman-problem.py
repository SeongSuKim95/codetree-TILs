n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

visited = [False] * (n+1)
arr = []
answer = 1e9
def choose(idx):
    global answer
    if idx == n - 1 :
        route = [1] + arr + [1]
        cost = 0
        for i in range(n):
            cost += grid[route[i]-1][route[i+1]-1]
        answer = min(answer,cost)
        return

    for i in range(2,n+1):
        
        if visited[i] :
            continue
        
        visited[i] = True
        arr.append(i)
        choose(idx+1)
        
        arr.pop()
        visited[i] = False

choose(0)
print(answer)