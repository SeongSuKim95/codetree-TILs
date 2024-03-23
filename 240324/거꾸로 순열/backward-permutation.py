n = int(input())

arr = []
visited = [False] * (n+1)

def choose(idx):

    if idx == n :
        print(*arr)
        return

    for i in range(n,0,-1):
        if visited[i]:
            continue

        visited[i] = True
        arr.append(i)
        choose(idx+1)

        arr.pop()
        visited[i] = False

choose(0)