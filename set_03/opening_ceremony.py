import sys
import bisect


def solve():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n = data[0]
    h = data[1 : 1 + n]
    h.sort()

    best = n

    i = 0
    while i < n:
        v = h[i]
        print(f"Considering height {v}")
        j = bisect.bisect_right(h, v)
        print(f"  Next distinct height at index {j}, value {h[j] if j < n else 'N/A'}")
        count_gt = n - j
        print(f"  Towers taller than {v}: {count_gt}")
        print(f"  min({best, v + count_gt})")
        best = min(best, v + count_gt)
        print(f"  Current best: {best}")
        i = j
        print()

    print(best)


if __name__ == "__main__":
    solve()
