import sys
sys.stdin = open("피자굽기_input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    C = [(idx+1, val) for idx, val in enumerate(list(map(int, input().split())))]
    A = []
    for _ in range(N):
        c = C.pop(0)
        A.append(c)
    while A:
        a, b = A.pop(0)
        k = b // 2
        if k == 0:
            if C:
                A.append(C.pop(0))
        elif k > 0:
            A.append((a, k))
    print("#{} {}".format(tc, a))

