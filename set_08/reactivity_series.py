import sys
from collections import deque


def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    K = int(next(it))

    g = [[] for _ in range(N)]
    indeg = [0] * N

    # Build graph
    for _ in range(K):
        a = int(next(it))
        b = int(next(it))
        g[a].append(b)
        indeg[b] += 1

    # Topological sort (Kahn’s algorithm)
    q = deque([i for i in range(N) if indeg[i] == 0])
    order = []

    while q:
        if len(q) > 1:
            print("back to the lab")
            return
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(order) != N:
        print("back to the lab")
    else:
        print(" ".join(map(str, order)))


if __name__ == "__main__":
    main()
