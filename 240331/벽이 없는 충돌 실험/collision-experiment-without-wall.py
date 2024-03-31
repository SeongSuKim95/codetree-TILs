from collections import defaultdict

def convertInput(inputList):
    x,y,w,d = inputList
    dirMap = {
        "U" : 0,
        "D" : 1,
        "R" : 2,
        "L" : 3
    }
    x,y = 2 * (x + 1001) - 1 ,2 * (y + 1001) - 1
    d = dirMap[d]
    return [x,y,w,d]

dxs,dys = [0,0,1,-1],[1,-1,0,0]

def move():

    global ballPos,occuredTime
    for elapsedTime in range(1,4003):
        nextballPos = defaultdict(list)
        for curPos,ballList in ballPos.items():
            cx,cy = curPos
            # print(curPos,ballList)
            for curball in ballList:
                cw,cnum,cdir = curball
                nx,ny = cx + dxs[cdir], cy + dys[cdir]
                nextballPos[(nx,ny)].append((cw,cnum,cdir))

        # print("Elapsed Time : ",elapsedTime)
        # for key,value in ballPos.items():
        #     print(key,value)
        # print()

        for nextPos,nextballList in nextballPos.items():
            if len(nextballList) > 1 :
                nextballPos[nextPos] = [tuple(sorted(nextballList,key = lambda x :(-x[0],-x[1]))[0])]
                occuredTime = elapsedTime
        
        ballPos = nextballPos


T = int(input()) # Test 케이스 개수
for _ in range(T):
    N = int(input()) # 구슬의 개수
    # 1번 부터 N번 구슬 정보 (x,y,w,d)
    balls = [
        convertInput(list(map(lambda x : x if x.isalpha() else int(x),input().split()))) for _ in range(N)
    ]

    ballPos = dict()
    occuredTime = -1
    for num,(x,y,w,d) in enumerate(balls):
        ballPos[(x,y)] = [(w,num+1,d)]
    
    move()

    print(occuredTime)