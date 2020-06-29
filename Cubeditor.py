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

pat = input()
lps = [0] * len(pat)
next(pat, lps)
print(lps)