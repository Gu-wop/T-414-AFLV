import sys

data = sys.stdin.read().strip()
N = int(data) if data else 0

result = pow(2, N) - N - 1

print(result)
