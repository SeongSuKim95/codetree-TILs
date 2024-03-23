n,m = list(map(int,input().split()))

selected = []
answer = 0
def selectNum(curr_num, cnt):
    global answer

    if cnt == m :
        xor = 0
        for elem in selected:
            xor ^= elem
        answer = max(xor,answer)
        return
    if curr_num == n+1:
        return
        
    selected.append(curr_num)
    selectNum(curr_num+1,cnt + 1)
    selected.pop()

    selectNum(curr_num+1,cnt)


selectNum(1,0)
print(answer)