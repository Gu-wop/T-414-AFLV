import sys
from math import gcd

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

n = next(it)
q = next(it)
a = [next(it) for _ in range(n)]

size = 1
while size < n:
    size <<= 1

seg = [0] * (2 * size)
seg[size : size + n] = a
for i in range(size - 1, 0, -1):
    seg[i] = gcd(seg[i << 1], seg[i << 1 | 1])


def point_set(idx: int, val: int):
    """Set a[idx] = val, 1-based idx."""
    i = idx - 1 + size
    seg[i] = val
    i >>= 1
    while i:
        seg[i] = gcd(seg[i << 1], seg[i << 1 | 1])
        i >>= 1


def range_gcd(l: int, r: int) -> int:
    """GCD on [l, r], 1-based inclusive."""
    l = l - 1 + size
    r = r - 1 + size
    left_g = 0
    right_g = 0
    while l <= r:
        if l & 1:
            left_g = gcd(left_g, seg[l])
            l += 1
        if not (r & 1):
            right_g = gcd(seg[r], right_g)
            r -= 1
        l >>= 1
        r >>= 1
    return gcd(left_g, right_g)


out_lines = []
for _ in range(q):
    x = next(it)
    y = next(it)
    z = next(it)
    if x == 1:
        point_set(y, z)
    else:
        out_lines.append(str(range_gcd(y, z)))

sys.stdout.write("\n".join(out_lines))
