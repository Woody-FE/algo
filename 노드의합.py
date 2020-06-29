import sys
sys.stdin = open("노드의합_input.txt")

def search(s):
    if s == 0:
        return 0
    if V[s][2] == 0:
        a = search(V[s][0])
        b = search(V[s][1])
        V[s][2] = a+b
        return V[s][2]
    return V[s][2]

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    V = [[0, 0, 0] for _ in range(N+1)]
    for _ in range(M):
        num, val = map(int, input().split())
        V[num] = [0, 0, val]
    for i in range(1, N+1):
        if 2*i <= N:
            V[i][0] = i*2
        if 2*i+1 <= N:
            V[i][1] = i*2+1

    search(L)
    print("#{} {}".format(tc, V[L][2]))
