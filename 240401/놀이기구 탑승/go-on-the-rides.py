N = int(input())

EMPTY = 0

friendLists = [
    list(map(int,input().split()))
    for _ in range(N*N)
]

grid = [
    [EMPTY for _ in range(N)]
    for _ in range(N)
]

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def printArr(arr):

    for row in arr:
        print(*row)
    print()

def simulate():

    dxs, dys = [-1,1,0,0], [0,0,-1,1]
    friendDict = dict()
    for curNum,f1,f2,f3,f4 in friendLists:

        curFriendList = [f1,f2,f3,f4]
        friendDict[curNum] = curFriendList

        checkList = []
        
        # 격자 내부 전부 탐색
        for i in range(N):
            for j in range(N):
                if grid[i][j] == EMPTY: # 비어있는 칸에 대해
                    curx, cury = i,j
                    emptyCnt, friendCnt = 0,0
                    for dx,dy in zip(dxs,dys):
                        nx,ny = curx+dx,cury+dy
                        if inRange(nx,ny) :
                            if grid[nx][ny] == EMPTY : 
                                emptyCnt += 1
                            if grid[nx][ny] in curFriendList:
                                friendCnt += 1
                    checkList.append((-friendCnt,-emptyCnt,curx,cury))
        
        checkList.sort()
        _,_,destx,desty = checkList[0]
        grid[destx][desty] = curNum
    
    score = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for dx,dy in zip(dxs,dys):
                nx,ny = i+dx, j+dy
                if inRange(nx,ny):
                    if grid[nx][ny] in friendDict[grid[i][j]]:
                        cnt += 1
            score += int(10 ** (cnt-1))

                
    return score


print(simulate())

# printArr(grid)