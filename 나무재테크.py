N, M, K = map(int, input().split())
# N 땅 넓이, M개의 나무, K년 후
# A는 겨울에 추가되는 양분
A = [list(map(int, input().split())) for _ in range(N)]
# x = row, y = col, z = age 나무나이
MAP = [[[[], []] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    MAP[x-1][y-1][0] += [z]

yang = [[5] * N for _ in range(N)]
delta = [(-1,-1), (-1,0), (-1,1), (0, -1), (0, 1), (1,-1), (1, 0), (1, 1)]
cnt = 0

while K:
    for i in range(N):
        for j in range(N):
            if MAP[i][j]:
                # 봄
                MAP[i][j][0].sort()
                b = -1
                for k in range(len(MAP[i][j][0])):
                    if yang[i][j] - MAP[i][j][0][k] < 0:
                        b = k
                        break
                    yang[i][j] -= MAP[i][j][0][k]
                    MAP[i][j][0][k] += 1
                if b != -1:
                    MAP[i][j][0], MAP[i][j][1] = MAP[i][j][0][:b], MAP[i][j][0][b:]
                else:
                    MAP[i][j][1] = []
                # 여름
                # 썩은 나무 제거
                for w in MAP[i][j][1]:
                    yang[i][j] += (w // 2)
    for i in range(N):
        for j in range(N):
            if MAP[i][j]:
                # 가을
                for a in range(len(MAP[i][j][0])):
                    if MAP[i][j][0][a] % 5 == 0:
                        for di, dj in delta:
                            ci, cj = i+di, j+dj
                            if 0 <= ci < N and 0 <= cj < N:
                                MAP[ci][cj][0] += [1]
            # 겨울
            yang[i][j] += A[i][j]
    K -= 1

for i in range(N):
    for j in range(N):
        if MAP[i][j]:
            cnt += len(MAP[i][j][0])
print(cnt)


