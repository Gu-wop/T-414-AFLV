import sys

# ---------- input ----------
it = iter(sys.stdin.buffer.read().split())
n = int(next(it))
m = int(next(it))
grid = [next(it).decode() for _ in range(n)]


def to_id(r, c):
    return r * m + c


def from_id(idx):
    return divmod(idx, m)


N = n * m

nxt = [0] * N
for r in range(n):
    row = grid[r]
    for c in range(m):
        ch = row[c]
        if ch == "^":
            nr, nc = r - 1, c
        elif ch == "v":
            nr, nc = r + 1, c
        elif ch == "<":
            nr, nc = r, c - 1
        else:
            nr, nc = r, c + 1  # '>'
        nxt[to_id(r, c)] = to_id(nr, nc)

# binary lifting table up[p][i] = node after 2^p steps from i
MAXP = 31  # since k <= 1e9 < 2^30, 31 is safe
up = [nxt[:]]
for p in range(1, MAXP):
    prev = up[p - 1]
    cur = [0] * N
    for i in range(N):
        cur[i] = prev[prev[i]]
    up.append(cur)

# ---------- answer queries ----------
q = int(next(it))
out_lines = []
for _ in range(q):
    x = int(next(it)) - 1
    y = int(next(it)) - 1
    k = int(next(it))

    node = to_id(x, y)
    p = 0
    while k:
        if k & 1:
            node = up[p][node]
        k >>= 1
        p += 1

    r, c = from_id(node)
    out_lines.append(f"{r+1} {c+1}")

sys.stdout.write("\n".join(out_lines))
