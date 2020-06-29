from collections import deque

def bfs():
    global min_count
    while q:
        x, y, string = q.popleft()
        if string == 'J':
            if x == 0 or x == r-1 or y == 0 or y == c-1:
                min_count = min(distance[x][y]+1, min_count)
        for dx, dy in delta:
            cx, cy = x + dx, y + dy
            if 0 <= cx < r and 0 <= cy < c:
                if MAP[cx][cy] == '.' and distance[cx][cy] == -1:
                    MAP[cx][cy] = string
                    distance[cx][cy] = distance[x][y] + 1
                    q.append((cx,cy,string))

r, c = map(int, input().split())
MAP = [list(input()) for _ in range(r)]
delta = [(0,1),(0, -1),(-1,0),(1,0)]
distance = [[-1] * c for _ in range(r)]
q = deque()
min_count = 123456789
for i in range(r):
    for j in range(c):
        if MAP[i][j] == 'F':
            q.append((i,j,'F'))
            distance[i][j] = 0
for i in range(r):
    for j in range(c):
        if MAP[i][j] == 'J':
            q.append((i,j,'J'))
            distance[i][j] = 0
bfs()
if min_count == 123456789:
    print("IMPOSSIBLE")
else:
    print(min_count)
