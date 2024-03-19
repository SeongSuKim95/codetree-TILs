K, N = list(map(int,input().split()))

answer = []

def choose(idx):

    if idx == N + 1:
        print(*answer)
        return 

    for i in range(1,K+1):
        answer.append(i)
        choose(idx+1)
        answer.pop()

choose(1)