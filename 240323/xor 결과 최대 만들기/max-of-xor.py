n,m = list(map(int,input().split()))
lst = list(map(int,input().split()))
selected = []
answer = 0
def selectNum(curr_idx, cnt):
    global answer

    if cnt == m :
        xor = 0
        for elem in selected:
            xor ^= elem
        answer = max(xor,answer)
        return

    if curr_idx == n:
        return

    selected.append(lst[curr_idx])
    selectNum(curr_idx+1,cnt + 1)
    selected.pop()

    selectNum(curr_idx+1,cnt)


selectNum(0,0)
print(answer)