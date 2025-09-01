import sys

def shortest_pattern_len(s: str) -> int:
    n = len(s)
    lps = [0] * n
    k = 0
    for i in range(1, n):
        while k > 0 and s[i] != s[k]:
            k = lps[k - 1]
        if s[i] == s[k]:
            k += 1
        lps[i] = k
    return n - lps[-1]

def main():
    data = sys.stdin.read().splitlines()
    t = int(data[0].strip())
    for i in range(1, t + 1):
        s = data[i].rstrip("\n")
        print(shortest_pattern_len(s))

if __name__ == "__main__":
    main()
