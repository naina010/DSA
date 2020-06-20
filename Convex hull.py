# Convex hull algorithm

from functools import reduce

def convex_hull(coordinates, n):
    if n<3:
        return
    def change(a, b, c):
    # check if on right -> returns true if 'c' is on right of line 'ab'
        return (((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])) < 0)

    def left(h, r):
        while len(h) > 1 and change(h[-2], h[-1], r):
            h.pop()
        # if not len(h) or h[-1]!=r:
        h.append(r)
        return h

    coordinates.sort(key=lambda x: x[1])
    coordinates.sort()

    lower = reduce(left, coordinates, [])
    upper = reduce(left, reversed(coordinates), [])
    lower.extend(upper[1:len(upper) - 1])
    return lower


coordinates = [[0,3], [2,2], [1,1], [2,1], [3,0], [0,0], [3,3]]
hull = convex_hull(coordinates, len(coordinates))
print(hull)
