n,m = list(map(int,input().split()))

selected = []
answer = 0
def selectNum(curr_num, cnt):
    global answer

    if curr_num == n + 1:
        if cnt == m :
            xor = 1
            for elem in selected:
                xor ^= elem
            # print(selected,xor)
            answer = max(xor,answer)
        return

    selected.append(curr_num)
    selectNum(curr_num+1,cnt + 1)
    selected.pop()

    selectNum(curr_num+1,cnt)


selectNum(1,0)
print(answer)