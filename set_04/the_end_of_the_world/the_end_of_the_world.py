def solve_hanoi():
    while True:
        line = input().strip()
        if line == "X":
            break

        state = line
        n = len(state)

        print(f"State: {state}, A, B, C, n={n}")
        moves_made = calculate_moves_made(state, "A", "B", "C", n)

        total_moves = (1 << n) - 1
        # total_moves = (2 ** n) - 1

        remaining = total_moves - moves_made
        print(remaining)


def calculate_moves_made(state, source, target, auxiliary, n):
    if n == 0:
        return 0

    if n == 1:
        if state[0] == source:
            print(f"n={n}, disk on source {source}, no moves\n")
            return 0
        elif state[0] == target:
            print(f"n={n}, disk on target {target}, 1 move\n")
            return 1
        else:
            print(f"n={n}, disk on auxiliary {auxiliary}, 2 moves\n")
            return 1

    largest_disk_pos = state[n - 1]

    if largest_disk_pos == source:
        print(f"n={n}, largest disk on source {source}, no moves for largest")
        print(f"state[: n - 1] = {state[: n - 1]}\n")
        return calculate_moves_made(state[: n - 1], source, auxiliary, target, n - 1)

    elif largest_disk_pos == target:
        print(f"n={n}, largest disk on target {target}, moves for largest\n")
        moves_to_clear_top = (1 << (n - 1)) - 1
        # moves_to_clear_top = (2 ** (n - 1)) - 1

        moves_largest = 1
        moves_remaining = calculate_moves_made(
            state[: n - 1], auxiliary, target, source, n - 1
        )
        print(
            f"n={n}, moves_to_clear_top={moves_to_clear_top}, moves_largest={moves_largest}, moves_remaining={moves_remaining}\n"
        )
        return moves_to_clear_top + moves_largest + moves_remaining

    else:
        moves_to_clear_top = (1 << (n - 1)) - 1
        # moves_to_clear_top = (2 ** (n - 1)) - 1

        moves_largest = 1
        print(
            f"n={n}, moves_to_clear_top={moves_to_clear_top}, moves_largest={moves_largest}\n"
        )
        return moves_to_clear_top + moves_largest


if __name__ == "__main__":
    solve_hanoi()
