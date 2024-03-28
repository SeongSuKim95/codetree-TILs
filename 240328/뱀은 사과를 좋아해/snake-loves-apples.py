# 변수 선언 및 입력
n, m, K = tuple(map(int, input().split()))
apple = [
    [False for _ in range(n + 1)]
    for _ in range(n + 1)
]
# 뱀은 처음에 (1, 1)에서 길이 1의 상태로 있습니다.
snake = [(1, 1)]

# 입력으로 주어진 방향을 정의한 dx, dy에 맞도록
# 변환하는데 쓰이는 dict를 정의합니다.
mapper = {
    'D': 0,
    'U': 1,
    'R': 2,
    'L': 3
}

ans = 0


# (x, y)가 범위 안에 들어가는지 확인합니다.
def can_go(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 뱀이 꼬였는지 확인합니다.
def is_twisted(new_head):
    return new_head in snake


# 새로운 머리를 추가합니다.
def push_front(new_head):
    # 몸이 꼬이는 경우
    # false를 반환합니다.
    if is_twisted(new_head):
        return False
    
    # 새로운 머리를 추가합니다.
    snake.insert(0, new_head)
    
    # 정상적으로 머리를 추가했다는 의미로
    # True를 반환합니다.
    return True


# 꼬리를 지웁니다.
def pop_back():
    snake.pop()


# (nx, ny)쪽으로 뱀을 움직입니다.
def move_snake(nx, ny):
    # 머리가 이동할 자리에 사과가 존재하면
    # 사과는 사라지게 되고
    if apple[nx][ny]:
        apple[nx][ny] = False
        # 꼬리는 사라지지 않고 머리만 늘어납니다.
        # 늘어난 머리때문에 몸이 꼬이게 된다면
        # False를 반환합니다.
        if not push_front((nx, ny)):
            return False
    else:
        # 사과가 없으면 꼬리는 사라지게 되고
        pop_back()
        
        # 머리는 늘어나게 됩니다.
        # 늘어난 머리때문에 몸이 꼬이게 된다면
        # False를 반환합니다.
        if not push_front((nx, ny)):
            return False
    
    # 정상적으로 뱀이 움직였으므로
    # True를 반환합니다.
    return True


# 뱀을 move_dir 방향으로 num번 움직입니다.
def move(move_dir, num):
    global ans
    
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    
    # num 횟수만큼 뱀을 움직입니다.
    # 한 번 움직일때마다 답을 갱신합니다.
    for _ in range(num):
        ans += 1
        
        # 뱀의 머리가 그다음으로 움직일
        # 위치를 구합니다.
        (head_x, head_y) = snake[0]
        nx = head_x + dxs[move_dir]
        ny = head_y + dys[move_dir]
        
        # 그 다음 위치로 갈 수 없다면
        # 게임을 종료합니다.
        if not can_go(nx, ny):
            return False
        
        # 뱀을 한 칸 움직입니다.
        # 만약 몸이 꼬인다면 False를 반환합니다.
        if not move_snake(nx, ny):
            return False
    
    # 정상적으로 명령을 수행했다는 의미인 True를 반환합니다.
    return True


# 사과가 있는 위치를 표시합니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    apple[x][y] = True

# K개의 명령을 수행합니다.
for _ in range(K):
    # move_dir 방향으로 num 횟수 만큼 움직여야 합니다.
    move_dir, num = tuple(input().split())
    num = int(num)
    
    # 움직이는 도중 게임이 종료되었을 경우
    # 더 이상 진행하지 않습니다.
    if not move(mapper[move_dir], num):
        break

print(ans)