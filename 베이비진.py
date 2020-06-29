import sys
sys.stdin = open("베이비진_input.txt")

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    A, B = [], []
    result = 0
    for i in range(len(arr)):
        if i%2 == 0:
            A.append(arr[i])
            if A.count(arr[i]) == 3:
                result = 1
                break
            if arr[i]-1 in A and arr[i]-2 in A:
                result = 1
                break
            if arr[i]-1 in A and arr[i]+1 in A:
                result = 1
                break
            if arr[i]+1 in A and arr[i]+2 in A:
                result = 1
                break
        else:
            B.append(arr[i])
            if B.count(arr[i]) == 3:
                result = 2
                break
            if arr[i]-1 in B and arr[i]-2 in B:
                result = 2
                break
            if arr[i]-1 in B and arr[i]+1 in B:
                result = 2
                break
            if arr[i]+1 in B and arr[i]+2 in B:
                result = 2
                break
    print("#{} {}".format(tc, result))