import sys


def compute_period(s):
    L = len(s)
    if L == 0:
        return 0
    pi = [0] * L
    j = 0
    for i in range(1, L):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
            print(f"  Mismatch at i={i}, j={j}. Backtrack j to pi[{j}]={j}")
        if s[i] == s[j]:
            j += 1
            print(f"  Match at i={i}, j={j-1}. Increment j to {j}")
        pi[i] = j
        print(f"  Set pi[{i}] = {j}")
    if pi[L - 1] == 0:
        return L
    return L - pi[L - 1]


input_data = sys.stdin.read().strip().splitlines()
N = int(input_data[0])
index = 1
for _ in range(N):
    s = input_data[index]
    index += 1
    print(compute_period(s))
