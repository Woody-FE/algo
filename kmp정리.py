def NEXT(pat, lps):
    length = len(pat)
    i, j = 1, 0
    while i < length:
        if pat[i] == pat[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
def searchKMP(txt, pat):
    t_len = len(txt)
    p_len = len(pat)
    i, j = 0, 0
    lps = [0] * p_len
    NEXT(pat, lps)
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
            print("{}좌표에서 매칭 성공".format(i-j))
            j = lps[j-1]
