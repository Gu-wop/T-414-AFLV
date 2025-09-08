import sys
import math

def solve_case(points):
    def feasible(R):
        left, right = -float('inf'), float('inf')
        R2 = R * R
        for x, y in points:
            ay = abs(y)
            if R < ay:
                return False, None, None
            dx = math.sqrt(max(0.0, R2 - y*y))
            left = max(left, x - dx)
            right = min(right, x + dx)
            if left > right:
                return False, None, None
        return True, left, right

    lo, hi = 0.0, 1.0
    ok, L, Rint = feasible(hi)
    while not ok:
        hi *= 2.0
        ok, L, Rint = feasible(hi)

    for _ in range(80):
        mid = (lo + hi) / 2.0
        ok, L, Rint = feasible(mid)
        if ok:
            hi = mid
            last_L, last_R = L, Rint
        else:
            lo = mid

    X = last_L
    T = hi
    return X, T

def main():
    tokens = iter(sys.stdin.read().strip().split())
    out_lines = []
    while True:
        try:
            n = int(next(tokens))
        except StopIteration:
            break
        if n == 0:
            break
        pts = []
        for _ in range(n):
            x = float(next(tokens)); y = float(next(tokens))
            pts.append((x, y))
        X, T = solve_case(pts)
        out_lines.append(f"{X:.12f} {T:.12f}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
