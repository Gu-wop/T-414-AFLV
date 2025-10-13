import sys


def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it))
    S, B = [], []
    for _ in range(n):
        s = int(next(it))
        b = int(next(it))
        S.append(s)
        B.append(b)

    best = float("inf")
    for mask in range(1, 1 << n):
        sour = 1
        bitter = 0
        for i in range(n):
            if mask & (1 << i):
                sour *= S[i]
                bitter += B[i]

        diff = abs(sour - bitter)
        if diff < best:
            best = diff

    print(best)


if __name__ == "__main__":
    main()
