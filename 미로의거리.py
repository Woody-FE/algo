from collections import deque
import sys
sys.stdin = open("미로의거리_input.txt")
def BFS(a, b):
    q = deque()
    q.append((a, b, 0))
    ck[a][b] = 1
    while q:
        x, y, cnt = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0 ,1)]:
            cx, cy = x + dx, y + dy
            if 0 <= cx < N and 0 <= cy < N:
                if MAP[cx][cy] == 3:
                    return cnt
                if ck[cx][cy] == 0 and MAP[cx][cy] == 0:
                    ck[cx][cy] = 1
                    q.append((cx, cy, cnt+1))
    return 0

for tc in range(1, int(input())+1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]
    ck = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                print("#{} {}".format(tc, BFS(i, j)))