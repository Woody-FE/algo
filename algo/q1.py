import sys
sys.stdin = open('q1_input.txt')

def sdoku(arr):
    for i in range(9):
        # 행을 고정으로 하고 열을 이동하면서 같은 요소가 있는지 체크
        if MAP[arr[0]][i] == arr[2]:
            return False
        # 열을 고정으로 하고 행을 이동시키면서 같은 요소가 있는지 체크
        if MAP[i][arr[1]] == arr[2]:
            return False
    x,y = arr[0] // 3, arr[1] // 3
    for i in range(3*x, 3*(x+1)):
        for j in range(3*y, 3*(y+1)):
            if MAP[i][j] == arr[2]:
                return False
    return True

for tc in range(1, int(input())+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(9)]
    cnt = 0
    check = True
    for _ in range(N):
        IDX = list(map(int, input().split()))
        if sdoku(IDX) and check:
            cnt += 1
        else:
            check = False
    print("#{} {}".format(tc, cnt))