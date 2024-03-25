from collections import deque

N = int(input())

def bfs():

    q = deque()
    q.append((N,0))
    while q :
        curNum,curCnt = q.popleft()
        if curNum == 1 :
            return curCnt

        nextNum = curNum - 1 
        q.append((nextNum,curCnt+1))

        nextNum = curNum + 1
        q.append((nextNum,curCnt+1))
        
        if curNum % 2 == 0:
            nextNum = curNum // 2
            q.append((nextNum,curCnt+1))

        if curNum % 3 == 0:
            nextNum = curNum // 3
            q.append((nextNum,curCnt+1))

print(bfs())