# digbuild.py
MOD = 10**9 + 7


def matmul(A, B):
    m = len(A)
    C = [[0] * m for _ in range(m)]
    for i in range(m):
        for k in range(m):
            if A[i][k]:
                aik = A[i][k]
                Bk = B[k]
                Ci = C[i]
                for j in range(m):
                    Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
    return C


def matpow(M, e):
    m = len(M)
    R = [[int(i == j) for j in range(m)] for i in range(m)]
    while e:
        if e & 1:
            R = matmul(R, M)
        M = matmul(M, M)
        e >>= 1
    return R


def solve():
    n = int(input().strip())

    # Valid column states for a 3×1 slice with no vertical adjacency:
    states = [0, 1, 2, 4, 5]  # 000,001,010,100,101
    m = len(states)

    # Build 5×5 compatibility matrix: allowed if no same-row torches
    A = [[0] * m for _ in range(m)]
    for i, a in enumerate(states):
        for j, b in enumerate(states):
            A[i][j] = 1 if (a & b) == 0 else 0

    if n == 1:
        print(m % MOD)  # 5
        return

    # Total ways with n columns:
    # dp[n] = A^(n-1) * dp[1], where dp[1] is all ones
    M = matpow(A, n - 1)
    # Sum of all entries of M equals sum(M * 1_vector) over all rows
    ans = sum(sum(row) for row in M) % MOD
    print(ans)


if __name__ == "__main__":
    solve()
