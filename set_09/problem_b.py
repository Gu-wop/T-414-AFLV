import sys
from collections import deque

INF = 10**30


def bellman_ford(n, edges, s):
    dist = [INF] * n
    dist[s] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    neg = [False] * n
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            neg[v] = True

    if any(neg):
        adj = [[] for _ in range(n)]
        for u, v, _ in edges:
            adj[u].append(v)
        q = deque([i for i, f in enumerate(neg) if f])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not neg[v]:
                    neg[v] = True
                    q.append(v)

    return dist, neg


def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    out_cases = []
    while True:
        n = int(next(it))
        m = int(next(it))
        q = int(next(it))
        s = int(next(it))
        if n == 0 and m == 0 and q == 0 and s == 0:
            break

        edges = []
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            w = int(next(it))
            edges.append((u, v, w))

        dist, neg = bellman_ford(n, edges, s)

        lines = []
        for _ in range(q):
            t = int(next(it))
            if neg[t]:
                lines.append("-Infinity")
            elif dist[t] == INF:
                lines.append("Impossible")
            else:
                lines.append(str(dist[t]))
        out_cases.append("\n".join(lines))

    sys.stdout.write("\n\n".join(out_cases))


if __name__ == "__main__":
    main()
