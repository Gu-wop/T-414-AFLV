import sys

data = sys.stdin.read().strip().split()
it = iter(data)
N = int(next(it))
K = int(next(it))
grid = [list(next(it)) for _ in range(N)]


def build_ps(mat):
    n = len(mat)
    m = len(mat[0])
    ps = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        row_ps = ps[i + 1]
        prev_row = ps[i]
        mi = mat[i]
        s = 0
        for j in range(m):
            s += mi[j]
            row_ps[j + 1] = prev_row[j + 1] + s
    return ps


def rect_sum(ps, r1, c1, r2, c2):
    return ps[r2][c2] - ps[r1][c2] - ps[r2][c1] + ps[r1][c1]


# Prepare matrices
bad = [[0] * N for _ in range(N)]
val = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        ch = grid[i][j]
        if ch != ".":
            bad[i][j] = 1
        if "1" <= ch <= "9":
            val[i][j] = ord(ch) - 48

PS_bad = build_ps(bad)
PS_val = build_ps(val)

ans = 0
inner = K - 2
for i in range(N - K + 1):
    for j in range(N - K + 1):
        total_bad = rect_sum(PS_bad, i, j, i + K, j + K)
        inner_bad = rect_sum(PS_bad, i + 1, j + 1, i + 1 + inner, j + 1 + inner)
        if total_bad - inner_bad == 0:
            inner_val = rect_sum(PS_val, i + 1, j + 1, i + 1 + inner, j + 1 + inner)
            if inner_val > ans:
                ans = inner_val

print(ans)
