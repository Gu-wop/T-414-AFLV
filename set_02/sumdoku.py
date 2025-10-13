import sys


def check_op(s, op):
    if op == "<":
        return s < 10
    elif op == "=":
        return s == 10
    elif op == ">":
        return s > 10
    return False


def can_place(grid, row, col, num, row_mask, col_mask, block_mask, constraints):
    bit = 1 << (num - 1)
    if row_mask[row] & bit:
        return False
    if col_mask[col] & bit:
        return False
    b = (row // 3) * 3 + (col // 3)
    if block_mask[b] & bit:
        return False

    for r1, c1, r2, c2, op in constraints:
        if r1 == row and c1 == col:
            other_r, other_c = r2, c2
            other_num = grid[other_r][other_c]
            if other_num != 0:
                s = num + other_num
                if not check_op(s, op):
                    return False
        elif r2 == row and c2 == col:
            other_r, other_c = r1, c1
            other_num = grid[other_r][other_c]
            if other_num != 0:
                s = num + other_num
                if not check_op(s, op):
                    return False
    return True


def solve(grid, pos, row_mask, col_mask, block_mask, constraints):
    if pos == 81:
        return True
    r = pos // 9
    c = pos % 9
    for num in range(1, 10):
        if can_place(grid, r, c, num, row_mask, col_mask, block_mask, constraints):
            grid[r][c] = num
            bit = 1 << (num - 1)
            row_mask[r] |= bit
            col_mask[c] |= bit
            b = (r // 3) * 3 + (c // 3)
            block_mask[b] |= bit
            if solve(grid, pos + 1, row_mask, col_mask, block_mask, constraints):
                return True
            grid[r][c] = 0
            row_mask[r] &= ~bit
            col_mask[c] &= ~bit
            block_mask[b] &= ~bit
    return False


def main():
    data = sys.stdin.read().splitlines()
    if len(data) < 15:
        return
    data = data[:15]

    horiz_idx = [0, 2, 4, 5, 7, 9, 10, 12, 14]
    vert_idx = [1, 3, 6, 8, 11, 13]
    horiz_const = [data[i] for i in horiz_idx]
    vert_const = [data[i] for i in vert_idx]

    constraints = []
    pairs_h = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8)]
    for r in range(9):
        syms = horiz_const[r]
        if len(syms) != 6:
            return
        for k in range(6):
            op = syms[k]
            c1, c2 = pairs_h[k]
            constraints.append((r, c1, r, c2, op))

    pairs_v = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8)]
    for k in range(6):
        syms = vert_const[k]
        if len(syms) != 9:
            return
        rr1, rr2 = pairs_v[k]
        for c in range(9):
            op = syms[c]
            constraints.append((rr1, c, rr2, c, op))

    grid = [[0 for _ in range(9)] for _ in range(9)]
    row_mask = [0] * 9
    col_mask = [0] * 9
    block_mask = [0] * 9

    solve(grid, 0, row_mask, col_mask, block_mask, constraints)

    for row in grid:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
