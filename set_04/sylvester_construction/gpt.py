import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        # n is unused except for bounds; we only need x,y,w,h
        n, x, y, w, h = data[idx : idx + 5]
        idx += 5

        cols = [x + i for i in range(w)]  # precompute columns for speed
        for r in range(y, y + h):
            # H[r,c] = (-1)^(bitcount(r & c))
            row = ["-1" if ((r & c).bit_count() & 1) else "1" for c in cols]
            out.append(" ".join(row))
        out.append("")  # blank line after each test case

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
