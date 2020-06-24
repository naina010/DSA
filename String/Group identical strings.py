def compute_hash(s):
    p = 31
    hash = 0
    mod = 10**9+7
    p_pow = 1
    for c in s:
        hash = (hash + (ord(c)-96)*p_pow)%mod
        p_pow = (p_pow*p)%mod
    return hash

def group_identical_strings(arr, n):
    string_hash = []
    for i in range(n):
        string_hash.append((compute_hash(arr[i]), i))   # O(N.M)
    string_hash.sort()                                  # O(NlogN)
    groups = [[string_hash[0][1]]]
    for i in range(1, n):
        if string_hash[i][0] == string_hash[i-1][0]:
            groups[-1].append(string_hash[i][1])
        else:
            groups.append([string_hash[i][1]])
    return groups
