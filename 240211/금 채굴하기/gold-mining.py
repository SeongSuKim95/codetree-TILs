n,m = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]

def isValid(x,y):

    return 0<=x<n and 0<=y<n

def isInRange(cur_x,cur_y,dist_x,dist_y,th):

    return (dist_x - cur_x) ** 2 + (dist_y - cur_y) ** 2 <= th ** 2

def checkGold(x,y):

    return grid[x][y] == 1

def findCost(cur_x,cur_y,cur_range):
    gold_cnt = 0 
    cost = cur_range ** 2 + (cur_range + 1) ** 2
    # 매번 N X N 완탐
    for dist_x in range(n):
        for dist_y in range(n):
            if isValid(dist_x,dist_y) and isInRange(cur_x,cur_y,dist_x,dist_y,cur_range) and checkGold(dist_x,dist_y):
                gold_cnt += 1
    return (gold_cnt * m - cost, gold_cnt)

def solve():
    answer = -1
    for i in range(n):
        for j in range(n):
            for cur_range in range(n):
                cost, gold_cnt = findCost(i,j,cur_range)
                if cost >= 0 :
                    answer = max(answer, gold_cnt)
    
    return answer

print(solve())