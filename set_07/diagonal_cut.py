import sys, math

M, N = map(int, sys.stdin.read().split())
g = math.gcd(M, N)
print(g if (M // g) % 2 == 1 and (N // g) % 2 == 1 else 0)
