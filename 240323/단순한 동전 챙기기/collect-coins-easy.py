N = int(input())

grid = [list(input()) for _ in range(N)]
numInfo = []
selectedNum = []
start,end = 0,0
answer = 1e9
for i in range(N):
    for j in range(N):
        curStr = grid[i][j]
        if curStr.isdigit(): 
            numInfo.append([int(curStr),(i,j)])
        if curStr == "S":
            start = [curStr,(i,j)]
        if curStr == "E":
            end = [curStr,(i,j)]
            
numInfo.sort(key = lambda x : x[0])

M = len(numInfo)
# print(numInfo,M)

def findRoute(lst):
    
    plen = len(lst)
    dist = 0
    for i in range(plen-1):
        dist += (abs(lst[i+1][1][0] - lst[i][1][0]) + abs(lst[i+1][1][1] - lst[i][1][1]))
    return dist

def selectNum(idx,cnt):
    global answer
    if M < 3:
        answer = -1
        return

    if cnt == 3 :
        points = [start] + selectedNum + [end]
        # print(*points)
        answer = min(answer,findRoute(points))
        return
    
    if idx == M:
        return
   
    selectedNum.append(numInfo[idx])
    selectNum(idx+1,cnt+1)
    selectedNum.pop()

    selectNum(idx+1,cnt)

selectNum(0,0)
print(answer)