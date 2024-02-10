n,m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
answer = 0
for idx in range(n):
    # 행 
    temp_row = grid[idx][:]
    # 열
    temp_col = [grid[col][idx] for col in range(n)]
                
    for temp in [temp_row,temp_col]:
        for cur_idx in range(n-m+1):
            cur_num = temp[cur_idx]
            cur_flag = True
            for cnt in range(1,m):
                if temp[cur_idx+cnt] != cur_num : 
                    cur_flag = False
                    break
            if cur_flag : 
                # print("Success case :",temp[:])
                answer += 1
                break
    
print(answer)