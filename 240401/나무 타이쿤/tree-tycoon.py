# 격자 크기, 년수
N,M = list(map(int,input().split()))

# 초기 리브로수 상태
trees = [
    list(map(int,input().split()))
    for _ in range(N)
]
# 약이 있으면 True, 없으면 False
medicines = [
    [0] * N 
    for _ in range(N)
]
# 초기 상태 
medicines[N-1][0] = 1
medicines[N-1][1] = 1
medicines[N-2][0] = 1
medicines[N-2][1] = 1

# dirs = [(0,0),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]
dirs = [(0,0),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]
diagDirs = [(-1,-1),(-1,1),(1,-1),(1,1)]

# 이동 방향 : 1 ~ 8
# (이동 방향, 이동 칸수)
moves = [
    tuple(map(int,input().split()))
    for _ in range(M)
]

def inRange(x,y):

    return 0<=x<N and 0<=y<N

def growTrees():
    
    for cx in range(N):
        for cy in range(N):
            if medicines[cx][cy]:
                trees[cx][cy] += 1
                
    newTrees = [
        [0] * N
        for _ in range(N)
    ]

    for cx in range(N):
        for cy in range(N):
            cnt = 0
            if medicines[cx][cy] :
                for dx,dy in diagDirs:
                    nx,ny = cx+dx, cy+dy
                    if inRange(nx,ny):
                        if trees[nx][ny]:
                            cnt += 1
                newTrees[cx][cy] = trees[cx][cy] + cnt
            else :
                newTrees[cx][cy] = trees[cx][cy]

    for i in range(N):
        for j in range(N):
            trees[i][j] = newTrees[i][j]
def cutTrees():
    newMedicines = [
        [0] * N 
        for _ in range(N)
    ]
    for i in range(N):
        for j in range(N):
            if not medicines[i][j]:
                if trees[i][j] >=2 :
                    newMedicines[i][j] = 1
                    trees[i][j] -= 2
            else :
                newMedicines[i][j] = 0
    
    for i in range(N):
        for j in range(N):
            medicines[i][j] = newMedicines[i][j]

def moveMedicines(curDir,curStep):

    nextMedicines = [
        [0] * N
        for _ in range(N)
    ]
    dx,dy = dirs[curDir]

    for cx in range(N):
        for cy in range(N):
            if medicines[cx][cy] :
                nx,ny = (cx + curStep * dx + N * curStep) % N, (cy + curStep * dy + N * curStep) % N,
                nextMedicines[nx][ny] = 1
    for i in range(N):
        for j in range(N):
            medicines[i][j] = nextMedicines[i][j]

def printArr(desc,arr):
    print(desc)
    print()
    for row in arr:
        print(*row)
    print()

def simulate():
   
    for curdir, curstep in moves:
        moveMedicines(curdir,curstep)
        growTrees()
        cutTrees()

    answer = 0

    for i in range(N):
        for j in range(N):
            answer += trees[i][j]

    return answer

print(simulate())