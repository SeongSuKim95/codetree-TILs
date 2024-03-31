# N, K = 무빙워크 윗판 길이, 안정성 0 인 개수 K (실험 끝)


# 4. 안정성이 0인 발판이 k개 이상이면 과정 종료
# 5. N번 칸에 사람이 있으면 즉시 내림

N, K = list(map(int,input().split()))

EMPTY = 0 # 사람이 없음을 표시
persons = {
    idx : EMPTY
    for idx in range(N)
}

safety = list(map(int,input().split()))

# 0 번 칸에 사람 , N-1 번에 끝

def shiftRight():
    global safety, persons

    safety = [safety[-1]] + safety[:-1]
    newPersons = {
        idx : EMPTY
        for idx in range(N)
    }    

    for i in range(1,N-1):
        newPersons[i] = persons[i-1]
    persons = newPersons

def simulate():
    personNumber,turn = 0,0
    while True:
        turn += 1
        # 1. 무빙워크 한 칸 회전
        shiftRight()
        
        # 즉시 하차
        persons[N-1] = EMPTY
        # 2. 가장 먼저 올라간 사람부터 무빙 워크 앞으로 한칸 이동
        # - 앞칸에 사람이 있으면 이동하지 않음
        # - 앞칸의 안정성이 0이면 이동하지 않음
        sortedIdx = sorted(persons.items(),key = lambda x : x[1])
        for position, personIdx in sortedIdx :
            if personIdx != EMPTY: # 위치, personIdx(올라간 순서)
                # 앞칸에 사람이 있으면 이동하지 않음
                if position + 1 <= N-1 and persons[position+1] != EMPTY:
                    continue
                # 앞칸의 안정성이 0 이면 이동하지 않음
                if position + 1 <= N-1 and safety[position+1] == 0 :
                    continue
                if position + 1 <= N-1 :
                    persons[position] = EMPTY
                    persons[position+1] = personIdx
                    safety[position+1] -= 1
                # 즉시 하차
                persons[N-1] = EMPTY

        # 3. 1번 칸에 사람이 없고 , 안정성이 0이 아니라면 사람을 추가
        if persons[0] == EMPTY and safety[0] != 0 :
            personNumber += 1
            persons[0] = personNumber
            safety[0] -= 1

        # 4. 안정성이 0인 발판이 k개 이상이면 과정 종료
        cnt = 0 
        for i in range(N):
            if safety[i] <= 0 :
                cnt += 1
        if cnt >= K :
            # print(safety)
            return turn

print(simulate())