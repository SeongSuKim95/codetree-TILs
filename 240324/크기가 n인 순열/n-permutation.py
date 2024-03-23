n = int(input())

visited = [False] * (n+1)
arr = []

def choose(idx):
    
    if idx == n :
        print(*arr)
        return
    
    for i in range(1,n+1):
        if visited[i]:
            continue

        visited[i] = True
        arr.append(i)
        choose(idx+1)
        
        arr.pop()
        visited[i] = False
    
choose(0)