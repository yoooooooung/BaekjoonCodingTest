N = int(input())
M = int(input())
snail = [[0]*N for _ in range(N)]

y, x = N//2, N//2
snail[y][x] = 1

i = 2
move = 1

# 가운데좌표부터 상, 우, 하, 좌 방향으로 달팽이 표 만들기
while i < N * N:
    # if x > 0
    # 위로
    for _ in range(move):
        if i <= N * N:
            y -= 1
            snail[y][x] = i
            i += 1

    # 오른쪽
    for _ in range(move):
        if i <= N * N:
            x += 1
            snail[y][x] = i
            i += 1
    else:
        move += 1

    # 아래로
    for _ in range(move):
        if i <= N * N:
            y += 1
            snail[y][x] = i
            i += 1

    # 왼쪽으로
    for _ in range(move):
        if i <= N * N:
            x -= 1
            snail[y][x] = i
            i += 1
    else:
        move += 1

# M숫자의 좌표 구하기
Y, X = 0, 0
for sy in range(N):
    for sx in range(N):
        print(snail[sy][sx], end=" ")
        if snail[sy][sx] == M:
            Y, X = sy+1, sx+1
    else:
        print()
print(Y, X)