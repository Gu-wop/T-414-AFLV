from collections import deque
import sys


def divide_fast(n, names, adj):
    color = [-1] * n
    q = deque()

    for s in range(n):
        if color[s] != -1:
            continue
        color[s] = 0
        q.append(s)

        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                elif color[v] == cu:
                    return None

    walter, jesse = [], []
    for i, name in enumerate(names):
        (walter if color[i] == 0 else jesse).append(name)
    return walter, jesse


def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    n = int(next(it))
    names = [next(it).decode() for _ in range(n)]
    name_to_idx = {name: i for i, name in enumerate(names)}

    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a = next(it).decode()
        b = next(it).decode()
        u = name_to_idx[a]
        v = name_to_idx[b]
        adj[u].append(v)
        adj[v].append(u)

    res = divide_fast(n, names, adj)
    if res is None:
        print("impossible")
    else:
        w, j = res
        sys.stdout.write(" ".join(w) + "\n" + " ".join(j) + "\n")


if __name__ == "__main__":
    main()
