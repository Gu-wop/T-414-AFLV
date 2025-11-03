import sys
from itertools import product

MOD = 10**9 + 7


def valid_states():
    """All 3-cell column patterns with no vertical touching (5 states)."""
    states = []
    for a, b, c in product([0, 1], repeat=3):
        if not (a == 1 and b == 1) and not (b == 1 and c == 1):
            states.append([a, b, c])
    return states


def count_non_ugly(n):
    """DP over columns using the 5 valid states."""
    states = valid_states()
    S = len(states)

    # compatibility[i][j] = states i and j can be adjacent (no horizontal touching)
    compatibility = [[True] * S for _ in range(S)]
    for i in range(S):
        for j in range(S):
            for r in range(3):
                if states[i][r] == 1 and states[j][r] == 1:
                    compatibility[i][j] = False
                    break

    dp = [1] * S  # first column: any valid state
    for _ in range(2, n + 1):
        new = [0] * S
        for j in range(S):
            total = 0
            for i in range(S):
                if compatibility[i][j]:
                    total += dp[i]
            new[j] = total % MOD
        dp = new

    return sum(dp) % MOD


def solve():
    n = int(sys.stdin.readline().strip())
    print(count_non_ugly(n))


if __name__ == "__main__":
    solve()
