import sys
import heapq


def dijkstra(n, adj, s):
    INF = 10**30
    dist = [INF] * n
    dist[s] = 0
    h = [(0, s)]
    while h:
        d, u = heapq.heappop(h)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(h, (nd, v))
    return dist


def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    cases_outputs = []
    for a, b, c, d in zip(it, it, it, it):
        n = int(a)
        m = int(b)
        q = int(c)
        s = int(d)
        if n == 0 and m == 0 and q == 0 and s == 0:
            break

        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            w = int(next(it))
            adj[u].append((v, w))

        dist = dijkstra(n, adj, s)

        out_lines = []
        INF = 10**30
        for _ in range(q):
            t = int(next(it))
            if dist[t] == INF:
                out_lines.append("Impossible")
            else:
                out_lines.append(str(dist[t]))
        cases_outputs.append("\n".join(out_lines))

    sys.stdout.write("\n\n".join(cases_outputs))


if __name__ == "__main__":
    main()
