import sys

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    n, w = data[0], data[1]
    e = data[2:2+n]

    def stacks_needed(H: int) -> int:
        return sum((x + H - 1) // H for x in e)

    lo, hi = 1, max(e)
    while lo < hi:
        mid = (lo + hi) // 2
        if stacks_needed(mid) <= w:
            hi = mid
        else:
            lo = mid + 1
    H = lo

    total = sum(e)
    print(w * H - total)

if __name__ == "__main__":
    main()
