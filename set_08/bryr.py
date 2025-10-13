import sys
from collections import deque


def zero_one_bfs(n, adj, start, goal):
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[start] = 0
    dq = deque([start])

    while dq:
        u = dq.popleft()
        du = dist[u]
        for v, w in adj[u]:  # w is 0 (double-lane) or 1 (single-lane bridge)
            if du + w < dist[v]:
                dist[v] = du + w
                if w == 0:
                    dq.appendleft(v)  # 0-cost edges first
                else:
                    dq.append(v)  # 1-cost edges later
    return dist[goal]


def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        # c = 1 → single-lane bridge (cost 1), c = 0 → double-lane (cost 0)
        adj[a].append((b, c))
        adj[b].append((a, c))

    ans = zero_one_bfs(n, adj, 1, n)
    print(ans)


if __name__ == "__main__":
    main()
