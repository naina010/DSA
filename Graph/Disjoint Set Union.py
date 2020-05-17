from sys import stdin

def root(arr, a):
    while arr[a] != a:
        arr[a] = arr[arr[a]]
        a = arr[a]
    return a

def weighted_union(arr, a, b):
    rootA = root(arr, a)
    rootB = root(arr, b)
    if rootA == rootB:
        return
    elif size[rootA] <= size[rootB]:
        arr[rootA] = rootB
        size[rootB] += size[rootA]
        size[rootA] = 0
    else:
        arr[rootB] = rootA
        size[rootA] += size[rootB]
        size[rootB] = 0

def find(a, b):
    if root(parent, a) == root(parent, b):
        return True
    return False

#input
n, m = map(int, stdin.readline().split())
size = [1] * (n + 1)
parent = [i for i in range(n+1)]
initialize(parent, n + 1)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    weighted_union(parent, a, b)


