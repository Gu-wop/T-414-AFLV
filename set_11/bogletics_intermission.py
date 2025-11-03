def minimum_moves(n, k_list):
    """
    Returns the minimum number of moves needed to arrange the items
    in the correct order given n items and their target locations k_list.
    """
    visited = [False] * n
    moves = 0

    for i in range(n):
        if not visited[i]:
            cycle_length = 0
            current = i

            # Follow the cycle
            while not visited[current]:
                visited[current] = True
                cycle_length += 1
                current = k_list[current] - 1  # Convert to 0-based index

            # Each cycle of length L > 1 takes L + 1 moves
            if cycle_length > 1:
                moves += cycle_length + 1

    return moves


# Example usage:
if __name__ == "__main__":
    n = int(input().strip())
    k_list = list(map(int, input().split()))
    print(minimum_moves(n, k_list))
