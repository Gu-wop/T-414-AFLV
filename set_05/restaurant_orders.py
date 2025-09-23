import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    it = iter(data)
    n = next(it)
    costs = [0] + [next(it) for _ in range(n)]
    m = next(it)
    orders = [next(it) for _ in range(m)]

    Smax = max(orders)

    dp = [-1] * (Smax + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        c = costs[i]
        for s in range(c, Smax + 1):
            if dp[s - c] == -1:
                continue
            if dp[s] == -1:
                if dp[s - c] == -2:
                    dp[s] = -2
                else:
                    dp[s] = i
            elif dp[s] >= 0:
                dp[s] = -2

    out_lines = []
    for S in orders:
        state = dp[S]
        if state == -1:
            out_lines.append("Impossible")
        elif state == -2:
            out_lines.append("Ambiguous")
        else:
            ans = []
            cur = S
            while cur > 0:
                i = dp[cur]
                ans.append(i)
                cur -= costs[i]

            ans.sort()
            out_lines.append(" ".join(map(str, ans)))

    print("\n".join(out_lines))


if __name__ == "__main__":
    solve()
