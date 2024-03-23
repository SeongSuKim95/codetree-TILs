n,m = list(map(int,input().split()))

points = [tuple(map(int,input().split())) for _ in range(n)]
selected = []
answer = 1e9
def getDist(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    return abs(x1-x2)**2 + abs(y1-y2)**2
    

def getMaximumdist(lst):
    dist = -1
    for i in range(m):
        for j in range(i+1,m):
            dist = max(dist,getDist(lst[i],lst[j]))

    return dist

def select(idx,cnt):
    global answer
    if cnt == m :
        maxdist = getMaximumdist(selected)
        answer = min(answer,maxdist)
        return

    if idx == n :

        return
    
    selected.append(points[idx])
    select(idx+1,cnt+1)
    selected.pop()

    select(idx+1,cnt)


select(0,0)
print(answer)