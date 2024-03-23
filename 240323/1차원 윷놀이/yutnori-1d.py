n,m,k = list(map(int,input().split()))

turns = list(map(int,input().split()))
# 턴의 수, 윷놀이판 길이, 말의 수
# 초기 말 상태 : [1] * k
# 턴당 갈 수 있는 거리 : [2,4,2,4]

assigned = []
answer = -1
def calc():
    horses = [1] * (k + 1)
    score = 0
    for turn, horse in zip(turns,assigned):
        horses[horse] += turn
    # print(horses)
    for horse in horses[1:] :
        if horse >= m :
            score += 1
    return score

def selectHorse(turnIdx):
    global answer
    if turnIdx == n : 
        answer = max(answer,calc())
        return
    
    for i in range(1,k+1):
        assigned.append(i)
        selectHorse(turnIdx+1)
        assigned.pop()

selectHorse(0)
print(answer)