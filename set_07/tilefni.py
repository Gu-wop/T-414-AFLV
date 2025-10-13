import sys


def is_kth_power(n, k):
    lo, hi = 2, n
    while lo <= hi:
        mid = (lo + hi) // 2
        val = pow(mid, k)
        if val == n:
            return True
        if val < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


def main():
    n = int(sys.stdin.readline().strip())

    for k in range(60, 1, -1):
        if is_kth_power(n, k):
            print(k)
            return
    print(1)


if __name__ == "__main__":
    main()
