n = int(input())

nums = list(map(int,input().split()))

summation = sum(nums)

selected = []
answer = 1e9
def selectNums(idx,cnt):
    global answer

    if idx == 2*n:
        return

    if cnt == n:
        sum1 = sum(selected)
        sum2 = abs(summation - sum1)
        answer = min(answer,abs(sum1-sum2))
        return
    
    selected.append(nums[idx])
    selectNums(idx+1,cnt+1)
    selected.pop()

    selectNums(idx+1,cnt)
    

selectNums(0,0)
print(answer)