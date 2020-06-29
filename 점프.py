def BFS():
    for x in range(N):
        for y in range(N):
            if memo[x][y] == 0 or (x == N-1 and y == N-1):
                continue
            else:
                jump = MAP[x][y]
                if x + jump < N:
                    memo[x+jump][y] += memo[x][y]
                if y + jump < N:
                    memo[x][y+jump] += memo[x][y]
    return memo[N-1][N-1]

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
memo = [[0 for _ in range(N)] for _ in range(N)]
memo[0][0] = 1
print(BFS())


