import sys
sys.stdin = open('최소생산비용_input.txt')

def search(k, n, number_sum):
    global min_num
    if number_sum > min_num:
        return
    if n == k:
        min_num = min(min_num, number_sum)
        return
    for i in range(n):
        if check[i] == 0:
            check[i] = 1
            search(k+1, n, number_sum+MAP[k][i])
            check[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    min_num = 123456789
    search(0, N, 0)
    print("#{} {}".format(tc, min_num))