import sys
sys.stdin = open("화물도크_input.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    arr = []
    cnt = 1
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append([a, b])
    arr.sort(key=lambda x: (x[1], x[0]))
    start, end = arr[0][0], arr[0][1]
    for i in range(1, len(arr)):
        if end <= arr[i][0]:
            start = arr[i][0]
            end = arr[i][1]
            cnt += 1
    print("#{} {}".format(tc, cnt))