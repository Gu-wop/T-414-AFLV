import sys

INF = 10**15


def floyd_warshall(n, dist):
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik >= INF:
                continue
            di = dist[i]
            ndk = dik
            for j in range(n):
                v = ndk + dk[j]
                if v < di[j]:
                    di[j] = v


def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    out = []
    while True:
        n = int(next(it))
        m = int(next(it))
        q = int(next(it))
        if n == 0 and m == 0 and q == 0:
            break

        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            w = int(next(it))
            if w < dist[u][v]:
                dist[u][v] = w

        floyd_warshall(n, dist)

        neg_inf = [[False] * n for _ in range(n)]
        neg_nodes = [k for k in range(n) if dist[k][k] < 0]
        if neg_nodes:
            for k in neg_nodes:
                for i in range(n):
                    if dist[i][k] >= INF:
                        continue
                    for j in range(n):
                        if dist[k][j] < INF:
                            neg_inf[i][j] = True

        for _ in range(q):
            u = int(next(it))
            v = int(next(it))
            if neg_inf[u][v]:
                out.append("-Infinity")
            elif dist[u][v] >= INF:
                out.append("Impossible")
            else:
                out.append(str(dist[u][v]))

        out.append("")

    sys.stdout.write("\n".join(out[:-1]))


if __name__ == "__main__":
    main()
