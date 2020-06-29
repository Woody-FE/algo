import sys
sys.stdin = open("회전_input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(M):
        a = A.pop(0)
        A.append(a)
    print("#{} {}".format(tc, A[0]))
