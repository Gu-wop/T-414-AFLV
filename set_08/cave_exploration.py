import sys

sys.setrecursionlimit(1_000_000)


def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))

    # Build graph; keep an id for each undirected edge
    g = [[] for _ in range(N)]
    edges = []
    for eid in range(M):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        g[u].append((v, eid))
        g[v].append((u, eid))

    # ---- 1) Find bridges (Tarjan) ----
    timer = 0
    tin = [-1] * N
    low = [0] * N
    is_bridge = [False] * M

    def dfs(u: int, peid: int = -1):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        for v, eid in g[u]:
            if eid == peid:  # don't go back through the same edge
                continue
            if tin[v] != -1:  # back-edge
                low[u] = min(low[u], tin[v])
            else:  # tree-edge
                dfs(v, eid)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    is_bridge[eid] = True

    dfs(0)  # graph is guaranteed connected; starting from 0 reaches all

    # ---- 2) Count nodes reachable from 0 without crossing any bridge ----
    stack = [0]
    seen = [False] * N
    seen[0] = True
    count = 0

    while stack:
        u = stack.pop()
        count += 1
        for v, eid in g[u]:
            if is_bridge[eid]:  # ignore flooded-susceptible tunnels
                continue
            if not seen[v]:
                seen[v] = True
                stack.append(v)

    print(count)


if __name__ == "__main__":
    main()
