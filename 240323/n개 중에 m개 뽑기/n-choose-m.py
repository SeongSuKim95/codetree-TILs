N, M = list(map(int,input().split()))

# N개 숫자 중 M개 고르기

ans = []

def select(idx,cnt):

    if idx == N :
        if cnt == M :
            print(*ans)
        return
            
    ans.append(idx+1)
    select(idx+1,cnt+1)
    ans.pop()

    select(idx+1,cnt)

select(0,0)