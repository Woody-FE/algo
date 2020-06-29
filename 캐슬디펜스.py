from itertools import combinations
from collections import deque
from copy import deepcopy
def bfs(people):
    cnt = 0
    a, b, c = people
    people = [(N, a), (N, b), (N, c)]
    for i in range(N-1, -1, -1):
        for j in range(M):
            if 
    # while q:
    #     x, y = q.popleft()
    #     if people[0][0] - 1 != x:
    #         people = [(x+1, a), (x+1, b), (x+1, c)]
    #     ck = False
    #     if abs(people[0][0] - x) + abs(people[0][1] - y) <= D:
    #         ck = True
    #     if abs(people[1][0] - x) + abs(people[1][1] - y) <= D:
    #         ck = True
    #     if abs(people[2][0] - x) + abs(people[2][1] - y) <= D:
    #         ck = True
    #
    #     if ck == True:
    #         cnt += 1





N, M, D = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
d = deque()

for i in range(N-1, -1, -1):
    for j in range(M):
        if MAP[i][j] == 1:
            d.append((i,j))
for people in combinations(range(0, 5), 3):
    q = deepcopy(d)
    bfs(people)
