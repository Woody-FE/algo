n, m = map(int, input().split())
dict_set = {k: [] for k in range(n+1)}
for _ in range(m):
    cal, a, b = map(int, input().split())
    dict_set