import sys

# Precompute powers of two up to 63
POW2 = [1]
for _ in range(63):
    POW2.append(POW2[-1] << 1)


def moves_used(state: str, src: str = "A", dst: str = "B", aux: str = "C") -> int:
    """How many moves have been made so far on the optimal path src->dst?"""
    n = len(state)
    if n == 0:
        return 0
    p = state[-1]  # largest disk's peg
    if p == src:
        # Still moving the top n-1 from src -> aux
        return moves_used(state[:-1], src, aux, dst)
    elif p == dst:
        # Finished moving largest; add 2^(n-1), then move n-1 from aux -> dst
        return POW2[n - 1] + moves_used(state[:-1], aux, dst, src)
    else:
        # Input guaranteed to be on an optimal path, so this shouldn't happen.
        # If you want to be defensive, raise an error here.
        raise ValueError("State not on the optimal A->B path.")


def main():
    out = []
    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue
        if s == "X":
            break
        n = len(s)
        used = moves_used(s, "A", "B", "C")
        total = (1 << n) - 1
        out.append(str(total - used))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
