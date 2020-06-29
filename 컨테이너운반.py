import sys
sys.stdin = open("컨테이너운반_input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    check_t = [0 for _ in range(len(t))]
    while w:
        container = w.pop(0)
        for i in range(len(t)):
            if check_t[i] == 0 and t[i] >= container:
                check_t[i] = container
                break
    print("#{} {}".format(tc, sum(check_t)))