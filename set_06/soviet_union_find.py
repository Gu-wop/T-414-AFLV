import sys

sys.setrecursionlimit(1 << 20)


def solve():
    it = iter(sys.stdin.buffer.read().split())
    n = int(next(it))
    q = int(next(it))

    parent = list(range(n + 1))
    root_ver = [0] * (n + 1)
    edge_ver = [0] * (n + 1)

    def find(x: int) -> int:
        p = parent[x]
        if p == x:
            return x
        r = find(p)
        if edge_ver[x] != root_ver[r]:
            parent[x] = x
            return x
        parent[x] = r
        edge_ver[x] = root_ver[r]
        return r

    out = []
    for _ in range(q):
        t = next(it).decode()
        if t == "a":
            x = int(next(it))
            y = int(next(it))
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx
                edge_ver[ry] = root_ver[rx]
        elif t == "b":
            x = int(next(it))
            r = find(x)
            root_ver[r] += 1
        else:
            x = int(next(it))
            out.append(str(find(x)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
