def solve_orders():
    # Read input
    n = int(input())
    costs = list(map(int, input().split()))
    m = int(input())
    orders = list(map(int, input().split()))

    def find_combinations(target, costs):
        combinations = []

        def backtrack(remaining, current_combo, start_item):
            if remaining == 0:
                # Found a valid combination
                combinations.append(current_combo[:])
                return

            if remaining < 0:
                return

            # Try each item starting from start_item to avoid duplicates
            for i in range(start_item, len(costs)):
                current_combo[i] += 1
                backtrack(remaining - costs[i], current_combo, i)
                current_combo[i] -= 1

        # Start backtracking with empty combination
        backtrack(target, [0] * len(costs), 0)
        return combinations

    # Process each order
    for order_total in orders:
        combinations = find_combinations(order_total, costs)

        if len(combinations) == 0:
            print("Impossible")
        elif len(combinations) > 1:
            print("Ambiguous")
        else:
            # Exactly one combination found
            combo = combinations[0]
            result = []

            # Convert combination counts to item numbers (1-indexed)
            for item_idx, count in enumerate(combo):
                for _ in range(count):
                    result.append(item_idx + 1)  # 1-indexed

            result.sort()  # Sort in ascending order
            print(" ".join(map(str, result)))


if __name__ == "__main__":
    solve_orders()
