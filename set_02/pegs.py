import sys

def idx(r, c):
    return r * (r + 1) // 2 + c

DIRS = [ (0, -1), (0, 1), (-1, -1), (-1, 0), (1, 0), (1, 1) ]

MOVES = []
N = 5
for r in range(N):
    for c in range(r + 1):
        for dr, dc in DIRS:
            r1, c1 = r + dr, c + dc
            r2, c2 = r + 2*dr, c + 2*dc 
            if 0 <= r1 < N and 0 <= c1 <= r1 and 0 <= r2 < N and 0 <= c2 <= r2:
                a = idx(r, c)
                p = idx(r1, c1)
                t = idx(r2, c2)
                MOVES.append((a, p, t))

def best(mask):
    res = mask.bit_count()
    for a, p, t in MOVES:
        if (mask >> a) & 1 and (mask >> p) & 1 and ((mask >> t) & 1) == 0:
            new_mask = mask
            new_mask &= ~(1 << a)
            new_mask &= ~(1 << p)
            new_mask |= (1 << t)
            res = min(res, best(new_mask))
    return res

def read_board_to_mask(stdin):
    mask = 0
    bit = 0
    lines = [line.strip() for line in stdin if line.strip() != ""]
    for r in range(5):
        tokens = lines[r].split()
        for c in range(r + 1):
            if tokens[c].lower() == 'x':
                mask |= (1 << bit)
            bit += 1
    return mask

def main():
    mask = read_board_to_mask(sys.stdin)
    print(best(mask))

if __name__ == "__main__":
    main()
