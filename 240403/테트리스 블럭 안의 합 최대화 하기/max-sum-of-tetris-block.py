# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited_pos = []
max_sum = 0


# 주어진 위치가 격자를 벗어나는지 여부를 반환합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


# 주어진 위치로 이동할 수 있는지 여부를 확인합니다.
def can_go(x, y):
    return in_range(x, y) and (x, y) not in visited_pos


# 주어진 위치에 대하여 가능한 모든 모양을 탐색하며 최대 합을 반환합니다.
def get_max_sum(cnt, sum_of_nums):
    if cnt == 4:
        global max_sum
        max_sum = max(max_sum, sum_of_nums)
        return
    
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    for (x, y) in visited_pos:
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            
            if can_go(new_x, new_y):
                visited_pos.append((new_x, new_y))
                get_max_sum(cnt + 1, sum_of_nums + grid[new_x][new_y])
                visited_pos.pop()
    
    return


# 격자의 각 위치에 대하여 탐색해줍니다.
for i in range(n):
    for j in range(m):
        visited_pos.append((i, j))
        get_max_sum(1, grid[i][j])
        visited_pos.pop()

print(max_sum)