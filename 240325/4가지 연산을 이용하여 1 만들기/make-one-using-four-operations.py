from collections import deque

N = int(input())
nums = set()

def bfs():

    q = deque()
    q.append((N,0))
    nums.add(q)

    while q :
        curNum,curCnt = q.popleft()
        if curNum == 1 :
            return curCnt

        nextNum = curNum - 1 
        if nextNum not in nums:
            q.append((nextNum,curCnt+1))
            nums.add(nextNum)

        nextNum = curNum + 1
        if nextNum not in nums:
            q.append((nextNum,curCnt+1))
            nums.add(nextNum)        

        if curNum % 2 == 0:
            nextNum = curNum // 2
            if nextNum not in nums:
                q.append((nextNum,curCnt+1))
                nums.add(nextNum)

        if curNum % 3 == 0:
            nextNum = curNum // 3
            if nextNum not in nums:
                q.append((nextNum,curCnt+1))
                nums.add(nextNum)

print(bfs())