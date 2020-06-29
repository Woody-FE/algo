def next(pat, lps):
    # lps는 패턴 길이만큼의 배열, pat는 패턴
    i, j = 1, 0
    length = len(pat)
    while i < length:
        if pat[i] == pat[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    print(lps)

def searchKMP(txt, pat):
    global cnt
    t_len = len(txt)
    p_len = len(pat)


    lps = [0] * p_len
    next(pat, lps)
    i, j = 0, 0
    while i < t_len:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == p_len:
            cnt += 1
            idx.append(i-j+1)
            j = lps[j-1]
text = input()
pattern = input()
cnt = 0
idx = []
searchKMP(text, pattern)
print(cnt)
for i in idx:
    print(i)