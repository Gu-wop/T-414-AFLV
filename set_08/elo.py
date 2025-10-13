import sys
from collections import deque


def calculate_max_elo(n, x, players):
    max_a = max(a for _, _, a in players)
    MAX_V = 5000 + max_a

    reachable = [False] * (MAX_V + 1)
    q = deque()

    if x <= MAX_V:
        reachable[x] = True
        q.append(x)

    while q:
        v = q.popleft()
        for L, R, a in players:
            if L <= v <= R:
                u = v + a
                if u <= MAX_V and not reachable[u]:
                    reachable[u] = True
                    q.append(u)

    for v in range(MAX_V, -1, -1):
        if reachable[v]:
            return v
    return x


def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it))
    x = int(next(it))
    players = []
    for _ in range(n):
        L = int(next(it))
        R = int(next(it))
        a = int(next(it))
        players.append((L, R, a))

    result = calculate_max_elo(n, x, players)
    print(result)


if __name__ == "__main__":
    main()
