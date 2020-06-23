# KMP Pattern matching algorithm : O(N)

def computeLPS(pattern):
    m = len(pattern)
    lps = [0] * m
    k = 0
    for q in range(1, m):
        while k>0 and pattern[k] != pattern[q]:
            k = lps[k-1]
        if pattern[k] == pattern[q]:
            k += 1
        lps[q] = k
    return lps

def KMPsearch(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = computeLPS(pattern)
    q = 0
    for i in range(n):
        while q>0 and pattern[q] != text[i]:
            q = lps[q-1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            print('Patter found at index:', i-m+1)
            q = lps[q-1]

text = 'ABABDABACDABABCABAB'
pattern = 'ABABCABAB'

KMPsearch(text, pattern)