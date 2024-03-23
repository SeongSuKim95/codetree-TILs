N, M = list(map(int,input().split()))

# N개 숫자 중 M개 고르기

ans = []
answers = []

def select(idx,cnt):

    if idx == N :
        if cnt == M :
            answers.append(ans[:])
        return

    select(idx+1,cnt)
    
    ans.append(idx+1)
    select(idx+1,cnt+1)
    ans.pop()

select(0,0)
for elem in sorted(answers):
    print(*elem)