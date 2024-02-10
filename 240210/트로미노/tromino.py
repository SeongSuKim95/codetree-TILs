n,m = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]
pairs = [
    [(-1,0),(0,1)], # 상 우
    [(-1,0),(0,-1)], # 상 좌
    [(1,0),(0,1)], # 하 우
    [(1,0),(0,-1)], # 하 좌
    [(1,0),(-1,0)], # 상 하
    [(0,1),(0,-1)] # 좌 우
    ]

def is_valid_coord(x,y):
    
    return 0<=x<n and 0<=y<m

def is_valid_pair(cx,cy,pair):
    dir1, dir2 = pair
    return is_valid_coord(cx+dir1[0],cy+dir1[1]) and is_valid_coord(cx+dir2[0],cy+dir2[1])

def check_sum():
    answer = 0
    for i in range(n):
        for j in range(m):
            cx,cy = i,j
            for pair in pairs:
                if is_valid_pair(cx,cy,pair) :
                    answer = max(answer,grid[cx][cy]+grid[cx+pair[0][0]][cy+pair[0][1]]+grid[cx+pair[1][0]][cy+pair[1][1]])
    return answer

print(check_sum())