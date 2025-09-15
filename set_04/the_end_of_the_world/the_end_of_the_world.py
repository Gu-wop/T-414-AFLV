def solve_hanoi():
    while True:
        line = input().strip()
        if line == "X":
            break

        state = line
        n = len(state)

        moves_made = calculate_moves_made(state, "A", "B", "C", n)

        total_moves = (1 << n) - 1

        remaining = total_moves - moves_made
        print(remaining)


def calculate_moves_made(state, source, target, auxiliary, n):
    if n == 0:
        return 0

    if n == 1:
        if state[0] == source:
            return 0
        elif state[0] == target:
            return 1
        else:
            return 1

    largest_disk_pos = state[n - 1]

    if largest_disk_pos == source:
        return calculate_moves_made(state[: n - 1], source, auxiliary, target, n - 1)

    elif largest_disk_pos == target:
        moves_to_clear_top = (1 << (n - 1)) - 1
        moves_largest = 1
        moves_remaining = calculate_moves_made(
            state[: n - 1], auxiliary, target, source, n - 1
        )
        return moves_to_clear_top + moves_largest + moves_remaining

    else:
        moves_to_clear_top = (1 << (n - 1)) - 1
        moves_largest = 1
        return moves_to_clear_top + moves_largest


if __name__ == "__main__":
    solve_hanoi()
