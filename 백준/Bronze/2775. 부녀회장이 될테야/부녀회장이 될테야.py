T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())
    people = [[0]*(n+1) for _ in range(k+1)]

    for i in range(k+1):
        for j in range(1, n+1):
            if i == 0:
                people[i][j] = j
            else:
                for w in range(1, j+1):
                    people[i][j] += people[i-1][w]

    print(people[k][n])
