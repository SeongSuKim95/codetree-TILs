from collections import deque

# 변수 선언 및 입력
n, q = tuple(map(int, input().split()))
grid_size = (1 << n)

grid = [
    list(map(int, input().split()))
    for _ in range(grid_size)
]

levels = list(map(int, input().split()))

next_grid = [
    [0 for _ in range(grid_size)]
    for _ in range(grid_size)
]

bfs_q = deque()
visited = [
    [0 for _ in range(grid_size)]
    for _ in range(grid_size)
]

# 방향은 편의상 오른쪽, 아래, 위, 왼쪽 순서대로 정의합니다. 
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]


def in_range(x, y):
    return 0 <= x and x < grid_size and 0 <= y and y < grid_size


def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y]


# BFS를 진행한 이후 해당 그룹의 크기를 반환합니다.
def bfs():
    group_size = 0
    
    # BFS 탐색을 수행합니다.
    while bfs_q:
        curr_x, curr_y = bfs_q.popleft()
        group_size += 1

        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy
            
            if can_go(new_x, new_y):
                bfs_q.append((new_x, new_y))
                visited[new_x][new_y] = True
                
    return group_size


# 남아있는 빙하의 총 양을 계산합니다.
def get_num_of_ices():
    return sum([
        grid[i][j]
        for i in range(grid_size)
        for j in range(grid_size)
    ])


# 얼음 군집 중 최대 크기를 구합니다.
def get_biggest_size():
    max_size = 0
    
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] and not visited[i][j]:
                # 시작 위치를 queue에 넣고 BFS를 진행합니다.
                # bfs 진행 이후 나온 그룹의 크기 중 최댓값을 찾습니다.
                visited[i][j] = True
                bfs_q.append((i, j))
                max_size = max(max_size, bfs())
    
    return max_size


# (start_row, start_col)에서 half_size 크기의 격자를 
# move_dir 방향으로 이동합니다.
def move(start_row, start_col, half_size, move_dir):
    for row in range(start_row, start_row + half_size):
        for col in range(start_col, start_col + half_size):
            next_row = row + dxs[move_dir] * half_size
            next_col = col + dys[move_dir] * half_size
            
            next_grid[next_row][next_col] = grid[row][col]


def rotate(level):
    # Step1.
    # rotate 이후의 상태를 저장할
    # 배열을 0으로 초기화합니다.
    for i in range(grid_size):
        for j in range(grid_size):
            next_grid[i][j] = 0
    
    box_size, half_size = (1 << level), (1 << (level - 1))
    
    # Step2. 조건에 맞게 회전을 진행합니다.
    
    # Step2-1. 회전할 2^L * 2^L 크기 격자의 왼쪽 위 모서리 위치를 잡습니다.
    for i in range(0, grid_size, box_size):
        for j in range(0, grid_size, box_size):
            # Step2-2. 움직여야하는 2^(L - 1) * 2^(L - 1) 크기 격자의
            #          왼쪽 위 모서리를 각각 잡아
            #          알맞은 방향으로 이동시킵니다.
            move(i, j, half_size, 0)
            move(i, j + half_size, half_size, 1)
            move(i + half_size, j, half_size, 2)
            move(i + half_size, j + half_size, half_size, 3)
    
    # Step3.
    # rotate 이후의 결과를 다시
    # grid 배열로 가져옵니다.
    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j] = next_grid[i][j]


# 인접한 곳에 있는 얼음의 수를 셉니다.
def get_neighbor_nums(curr_x, curr_y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        new_x, new_y = curr_x + dx, curr_y + dy
        
        if in_range(new_x, new_y) and grid[new_x][new_y]:
            cnt += 1
    
    return cnt


def melt():
    # Step1.
    # 녹은 이후의 상태를 저장할
    # 배열을 0으로 초기화합니다.
    for i in range(grid_size):
        for j in range(grid_size):
            next_grid[i][j] = 0
    
    # Step2.
    # 인접한 칸의 수가 3개 이하인 곳의 얼음을 
    # 찾아 1씩 녹입니다.
    
    for i in range(grid_size):
        for j in range(grid_size):
            cnt = get_neighbor_nums(i, j)
            # Step2-1. 녹는경우에는 1을 빼서 넣어줍니다.
            if grid[i][j] and cnt < 3:
                next_grid[i][j] = grid[i][j] - 1
            # Step2-2. 녹지 않는 경우에는 그대로 넣어줍니다.
            else:
                next_grid[i][j] = grid[i][j]
    
    # Step3.
    # 녹은 이후의 결과를 다시
    # grid 배열로 가져옵니다.
    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j] = next_grid[i][j]


# q번에 걸쳐 회전과 녹는 과정을 진행합니다.
for level in levels:
    if level:
        rotate(level)
    melt()

print(get_num_of_ices())
print(get_biggest_size())