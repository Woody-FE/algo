from collections import deque
import sys
sys.stdin = open("노드의거리_input.txt")
def BFS(start, end):
    q = deque()
    q.append(start)
    ck[start] = 1
    while q:
        n = q.popleft()
        if end == n:
            return ck[n] - 1
        for y in N[n]:
            if not ck[y]:
                ck[y] = ck[n] + 1
                q.append(y)
    return 0

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    N = [[] for _ in range(V+1)]
    ck = [0] * (V+1)
    for _ in range(E):
        S, G = map(int, input().split())
        N[S].append(G)
        N[G].append(S)
    st, ed = map(int, input().split())
    print("#{} {}".format(tc, BFS(st, ed)))