import sys
import heapq


def dijkstra(n, adj, s):
    INF = 10**30
    dist = [INF] * (n + 1)
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    n = int(next(it))
    m = int(next(it))
    b = int(next(it))
    g = int(next(it))

    low = [[] for _ in range(n + 1)]
    high = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        sgm = int(next(it))
        low[u].append((v, w - sgm))
        high[u].append((v, w + sgm))

    b_low = dijkstra(n, low, b)
    b_high = dijkstra(n, high, b)
    g_low = dijkstra(n, low, g)
    g_high = dijkstra(n, high, g)

    ans = []
    INF = 10**30
    for v in range(1, n + 1):
        if b_high[v] >= INF or g_high[v] >= INF:
            continue
        lo = max(b_low[v], g_low[v])
        hi = min(b_high[v], g_high[v])
        if lo <= hi:
            ans.append(str(v))

    if ans:
        print(" ".join(ans))
    else:
        print("Thessi leikur verdur sennilega leidinlegur")


if __name__ == "__main__":
    main()
