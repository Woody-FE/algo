import sys
sys.stdin = open("문제1_input.txt")

def dfs(x, y):
    for dx, dy in delta:
        cx, cy = x+dx, y+dy
        if 0 <= cx < 10 and 0 <= cy < 10:
            if check[cx][cy] == 0 and MAP[cx][cy] == 1:
                check[cx][cy] = 1
                dfs(cx, cy)


for tc in range(1, int(input())+1):
    MAP = [list(map(int, input().split())) for _ in range(10)]
    delta = [(-1,-1), (-1,0), (-1,1), (0,1), (0,-1), (1,-1), (1,1), (1,0)]
    check = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0
    for a in range(10):
        for b in range(10):
            if check[a][b] == 0 and MAP[a][b]:
                cnt += 1
                dfs(a, b)
    print("#{} {}".format(tc, cnt))