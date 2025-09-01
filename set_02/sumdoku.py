import sys


# Sumdoku solver (documented)
#
# This module implements a backtracking solver for a 9x9 variant of Sudoku
# called "Sumdoku" (similar to the task in some programming contests):
# - You must place digits 1..9 in each cell so that each row, column and
#   3x3 block contains no duplicate digits (standard Sudoku rule).
# - Additionally, there are binary constraints between some pairs of cells.
#   Each such constraint gives a relational operator ('<', '=', '>') which
#   applies to the sum of the two involved cell values and the constant 10.
#   For example:
#     op == '<' means (a + b) < 10
#     op == '=' means (a + b) == 10
#     op == '>' means (a + b) > 10
#
# The solver uses bitmasks for fast conflict checks on rows, columns and
# blocks, and a simple depth-first backtracking (trying numbers 1..9 for
# each cell in row-major order). All constraints are kept in a list of tuples
# of the form (r1, c1, r2, c2, op).


def check_op(s, op):
    """
    Evaluate the relational constraint for a sum s and operator op.

    Parameters:
    - s: integer sum of two cell values
    - op: one of '<', '=', '>' meaning compare s to 10

    Returns True when the condition holds, False otherwise.
    """
    if op == '<':
        return s < 10
    elif op == '=':
        return s == 10
    elif op == '>':
        return s > 10
    # If an unknown operator is provided, treat as unsatisfied.
    return False


def can_place(grid, row, col, num, row_mask, col_mask, block_mask, constraints):
    """
    Check if 'num' can be placed at (row, col) without violating
    Sudoku uniqueness rules or any Sumdoku pairwise constraints.

    Data structures used for fast checks:
    - row_mask: list of 9 integers, each bit i (0-based) set means number (i+1)
      already exists in that row.
    - col_mask: same idea for columns.
    - block_mask: there are 9 blocks (3x3). block index b = (row//3)*3 + (col//3).

    Using bitmasks lets us test membership with a single bitwise AND.

    Steps:
    1. Build a bit for the candidate number: bit = 1 << (num-1).
    2. If any of row_mask[row], col_mask[col], block_mask[b] already has that
       bit set, the number is already present and cannot be placed.
    3. Otherwise, check all pairwise Sumdoku constraints that involve this
       cell. If the other cell in a constraint already holds a non-zero
       value, evaluate the sum condition using check_op.

    Note: this function does not update any masks or the grid; it only tests
    whether placement would be valid.
    """
    # Create a single-bit mask for `num`: the bit at position (num-1).
    # Mapping (num -> bit):
    # 1 -> 0b000000001 (decimal 1)
    # 2 -> 0b000000010 (decimal 2)
    # 3 -> 0b000000100 (decimal 4)
    # ...
    # 9 -> 0b100000000 (decimal 256)
    # Example: num==3 -> bit = 1 << (3-1) == 0b100 (4).
    bit = 1 << (num - 1)

    # Row / column / block uniqueness tests using bitwise AND.
    # Each mask (row_mask[row], col_mask[col], block_mask[b]) stores bits for
    # numbers already placed. Testing (mask & bit) != 0 means `num` is present.
    # Example: row_mask[row] = 0b00001010 (decimal 10) means numbers {2,4}
    # are present. For num=2, bit=0b00000010 -> row_mask[row] & bit == 0b10
    # (non-zero) so num 2 cannot be placed.
    if row_mask[row] & bit:
        return False
    # Column test (same idea): non-zero means conflict.
    # Example: col_mask[col] = 0b00000100 (decimal 4) means {3} present.
    if col_mask[col] & bit:
        return False
    b = (row // 3) * 3 + (col // 3)
    # 3x3 block test. block index b computed above selects the right mask.
    # Example: block_mask[b] = 0b00000001 (decimal 1) means {1} present.
    if block_mask[b] & bit:
        return False

    # Pairwise sum constraints: each constraint is (r1, c1, r2, c2, op)
    for r1, c1, r2, c2, op in constraints:
        # If this cell is the first in the pair, check against the second
        if r1 == row and c1 == col:
            other_r, other_c = r2, c2
            other_num = grid[other_r][other_c]
            # Only check constraints when the partner cell already has a value
            if other_num != 0:
                s = num + other_num
                if not check_op(s, op):
                    return False
        # If this cell is the second in the pair, check against the first
        elif r2 == row and c2 == col:
            other_r, other_c = r1, c1
            other_num = grid[other_r][other_c]
            if other_num != 0:
                s = num + other_num
                if not check_op(s, op):
                    return False

    # No conflicts found
    return True


def solve(grid, pos, row_mask, col_mask, block_mask, constraints):
    """
    Recursive backtracking solver.

    Parameters:
    - grid: 9x9 list of lists with 0 for empty, 1..9 for placed digits
    - pos: linear index in row-major order (0..80). When pos==81, all
           cells have been assigned successfully.
    - row_mask, col_mask, block_mask: current occupancy bitmasks
    - constraints: list of pairwise constraints as described earlier

    Returns True when a complete valid assignment is found (grid mutated in
    place), False if no assignment is possible from this state.

    Algorithm details:
    - The solver proceeds in strict row-major order (pos 0..80). For each
      empty cell it tries numbers 1..9 in increasing order.
    - When a number is placed, the corresponding bits are set in the masks.
    - If recursion fails to find a solution, we backtrack: unset the cell and
      clear the bits from the masks.

    This is a straightforward depth-first search. It is not heavily
    optimized (no MRV, no constraint propagation beyond immediate checks),
    but bitmasks keep basic checks fast.
    """
    # If we've assigned all 81 cells, we've found a solution
    if pos == 81:
        return True

    r = pos // 9
    c = pos % 9

    # If the cell is already filled (non-zero) we should skip it. In this
    # particular implementation the grid is initially all zeros and we fill
    # every cell in order, but supporting pre-filled cells would just require
    # this check. Keep behavior the same as the original by attempting to
    # place a number regardless; to preserve compatibility, handle pre-filled
    # cells by skipping them.
    if grid[r][c] != 0:
        return solve(grid, pos + 1, row_mask, col_mask, block_mask, constraints)

    for num in range(1, 10):
        if can_place(grid, r, c, num, row_mask, col_mask, block_mask, constraints):
            # place the number
            grid[r][c] = num
            # Create the bit for the placed number (see mapping above).
            # Example: num=5 -> bit = 1 << 4 == 0b00010000 (decimal 16).
            bit = 1 << (num - 1)
            # Set the bit to mark presence in row/column/block using bitwise OR.
            # This adds `num` to the set represented by the mask.
            # Example: row_mask[r]=0b00000010 (has {2}), bit=0b00000100 (num=3)
            # -> row_mask[r] |= bit == 0b00000110 (now {2,3}).
            row_mask[r] |= bit
            col_mask[c] |= bit
            b = (r // 3) * 3 + (c // 3)
            # Set the bit in the block mask (same operation for the 3x3 block).
            block_mask[b] |= bit

            # recurse to next position
            if solve(grid, pos + 1, row_mask, col_mask, block_mask, constraints):
                return True

            # Backtrack: remove placed number and clear bits in masks.
            grid[r][c] = 0
            # Clearing a bit: mask &= ~bit clears the single bit for `num`.
            # Example: bit=0b00000100 (num=3), row_mask[r]=0b00000110 ({2,3})
            # -> row_mask[r] & ~bit == 0b00000010 (now {2}).
            # Note: Python's ~ is the bitwise complement; using & ~bit on a
            # small non-negative mask is the standard way to clear a bit.
            row_mask[r] &= ~bit
            col_mask[c] &= ~bit
            block_mask[b] &= ~bit

    # no number 1..9 worked here
    return False


def main():
    """
    Read input from stdin, parse constraints, solve the puzzle, and print
    the completed 9x9 grid.

    Expected input format (15 lines total): the original program expects
    exactly 15 lines describing horizontal and vertical constraint symbols.
    This parsing is tailored to the contest/problem that produced the file.

    The input layout used in this code (as in the original) is:
    - Lines indexed by horiz_idx contain horizontal symbols for each of 9 rows
      (6 symbols per row). Each symbol is applied between a specific pair of
      columns.
    - Lines indexed by vert_idx contain vertical symbols for 6 row-pairs.
      Each of these lines has 9 symbols (one per column) describing vertical
      relationships between two consecutive groups of rows.

    The code below copies the original file's parsing rules exactly and then
    builds a constraints list of (r1,c1,r2,c2,op).
    """
    data = sys.stdin.read().splitlines()
    # Expect at least 15 lines for the specific input format; otherwise exit.
    if len(data) < 15:
        return
    data = data[:15]

    # The indices used by the original program to pick horizontal and
    # vertical lines from the 15-line input. These are problem-specific.
    horiz_idx = [0, 2, 4, 5, 7, 9, 10, 12, 14]
    vert_idx = [1, 3, 6, 8, 11, 13]
    horiz_const = [data[i] for i in horiz_idx]
    vert_const = [data[i] for i in vert_idx]

    constraints = []

    # Horizontal pairs: the horizontal input lines contain 6 symbols per row
    # describing relations between these pairs of columns (pairs_h).
    pairs_h = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8)]
    for r in range(9):
        syms = horiz_const[r]
        # sanity: each horizontal row must have exactly 6 symbols
        if len(syms) != 6:
            return
        for k in range(6):
            op = syms[k]
            c1, c2 = pairs_h[k]
            # Add the constraint between (r,c1) and (r,c2)
            constraints.append((r, c1, r, c2, op))

    # Vertical pairs: vert_const contains 6 strings, each corresponding to a
    # pair of row indices (rr1, rr2). Each string has 9 characters, one per
    # column, giving the operator for that column between rr1 and rr2.
    pairs_v = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8)]
    for k in range(6):
        syms = vert_const[k]
        if len(syms) != 9:
            return
        rr1, rr2 = pairs_v[k]
        for c in range(9):
            op = syms[c]
            constraints.append((rr1, c, rr2, c, op))

    # Initialize empty grid and masks
    grid = [[0 for _ in range(9)] for _ in range(9)]
    row_mask = [0] * 9
    col_mask = [0] * 9
    block_mask = [0] * 9

    # Run solver starting at position 0
    solve(grid, 0, row_mask, col_mask, block_mask, constraints)

    # Print the solved grid (or a partial grid if unsolved). Each row is
    # printed as space-separated digits.
    for row in grid:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()