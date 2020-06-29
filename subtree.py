import sys
sys.stdin = open("subtree_input.txt")
def DFS(n):
    global cnt
    cnt += 1
    for y in V[n]:
        DFS(y)

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    V = [[] for _ in range(E+2)]
    cnt = 0
    A = list(map(int, input().split()))
    for i in range(0, 2*E, 2):
        V[A[i]] += [A[i+1]]
    DFS(N)
    print("#{} {}".format(tc, cnt))

