# 숫자별로 position을 관리

# 종료조건 : 선택한 숫자의 인접한 방향에 아무 숫자도 없을 시

# 이동시 대상 칸의 맨 위로 이동 + 자기 자신 위에 있는 숫자도 같이 이동
def inRange(x,y):
    return 0<=x<N and 0<=y<N

def printArr(arr):

    for row in arr:
        print(*row)
    print()

N, M = list(map(int,input().split()))

grid = [
    list(map(int,input().split())) for _ in range(N)
]

for i in range(N):
    for j in range(N):
        grid[i][j] = [grid[i][j]]

nums = list(map(int,input().split()))

dxs,dys = [-1,-1,-1,0,1,1,1,0],[-1,0,1,1,1,0,-1,-1]

numPos = dict()

for i in range(N):
    for j in range(N):
        numPos[grid[i][j][0]] = (i,j)

def move():

    for num in nums:
        # 현재 선택된 숫자가 있는 위치
        cx,cy = numPos[num]
        canMove = False
        maxNum = 0
        destx,desty = 0,0
        for dx,dy in zip(dxs,dys):
            nx,ny = cx+dx,cy+dy
            if inRange(nx,ny):
                if grid[nx][ny]: # 빈 배열이 아니라면
                    canMove = True
                    destNum = max(grid[nx][ny]) # list 내에서 가장 큰 값
                    if destNum > maxNum : 
                        maxNum,destx,desty = destNum,nx,ny
                        # print("maxNum",maxNum)
        # 움직일 수 없으면 다음 숫자로
        if not canMove : 
            # print("can't move")
            continue

        # 현재 숫자가 포함된 List 에 대해 현재 숫자의 위치 찾기
        curNumList = grid[cx][cy][:]
        cidx = 0
        for idx,curNum in enumerate(curNumList): 
            if curNum == num :
                cidx = idx
        willMoveList = curNumList[:cidx+1]
        # dest,desty --> 현재 선택된 숫자가 포함된 list가 옮겨갈 위치
        grid[destx][desty] = willMoveList + grid[destx][desty] # dest list 위로 옮기기
        # 현재 위치 비워주기
        grid[cx][cy] = curNumList[cidx+1:]
        # 현재 숫자 +  위치 업데이트
        for movedNum in willMoveList :
            numPos[movedNum] = (destx,desty) 
        # printArr(grid)
        # print(numPos)
        # print(num,cidx)
        # print("destx,desty",(destx,desty))
        # print("willMoveList :",willMoveList)
        # print()
        
move()

for i in range(N):
    for j in range(N):
        if grid[i][j]:
            print(*grid[i][j])
        else :
            print("None")