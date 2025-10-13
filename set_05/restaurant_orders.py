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
        print(dp)
        print(costs)
        c = costs[i]
        for s in range(c, Smax + 1):
            print(f"i={i}, s={s}, c={c}, s-c={s-c}, dp[s-c]={dp[s-c]}, dp[s]={dp[s]}")
            if dp[s - c] == -1:
                print(f"Skipping s={s} because dp[{s - c}] == -1\n")
                continue
            if dp[s] == -1:
                if dp[s - c] == -2:
                    print(f"Setting dp[{s}] = -2 because dp[{s - c}] == -2\n")
                    dp[s] = -2
                else:
                    print(f"Setting dp[{s}] = {i} because dp[{s - c}] == {dp[s - c]}\n")
                    dp[s] = i
            elif dp[s] >= 0:
                print(f"Setting dp[{s}] = -2 because dp[{s}] was already {dp[s]}\n")
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
