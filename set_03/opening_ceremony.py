import sys
import bisect

def solve():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n = data[0]
    h = data[1:1+n]
    h.sort()

    best = n

    i = 0
    while i < n:
        v = h[i]
        j = bisect.bisect_right(h, v, i)
        count_gt = n - j
        best = min(best, v + count_gt)
        i = j

    print(best)

if __name__ == "__main__":
    solve()
