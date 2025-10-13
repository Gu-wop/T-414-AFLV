def solve_chair_stacking(w, chair_counts):
    """
    PROBLEM ANALYSIS:
    - We have chairs of different colors that must be grouped by color
    - Room width = w meters, so we can have at most w stacks
    - Each stack occupies 1 meter width
    - Goal: minimize disorganization = w * max_height - total_chairs

    KEY INSIGHT:
    To minimize disorganization, we need to minimize max_height.
    But we're constrained by the room width (max w stacks).

    STRATEGY:
    Binary search for the minimum max_height that allows
    fitting all chairs within w stacks.
    """
    total_chairs = sum(chair_counts)

    # Binary search bounds:
    # - Minimum possible height: 1 (at least 1 chair per stack)
    # - Maximum possible height: max(chair_counts) (worst case: all chairs of one color in one stack)
    left, right = 1, max(chair_counts)

    def can_fit_with_max_height(max_height):
        """
        Check if we can fit all chairs using at most w stacks
        with given maximum stack height.

        For each color with 'count' chairs:
        - We need ceil(count / max_height) stacks
        - This is calculated as: (count + max_height - 1) // max_height
        """
        stacks_needed = 0

        for count in chair_counts:
            # Calculate stacks needed for this color
            # Using ceiling division: ceil(a/b) = (a + b - 1) // b
            stacks_for_this_color = (count + max_height - 1) // max_height
            stacks_needed += stacks_for_this_color

            # Early termination: if we already exceed w stacks, no point continuing
            if stacks_needed > w:
                return False

        return stacks_needed <= w

    # Binary search for minimum feasible max_height
    while left < right:
        mid = (left + right) // 2
        if can_fit_with_max_height(mid):
            # mid works, try to find smaller value
            right = mid
        else:
            # mid doesn't work, need larger value
            left = mid + 1

    max_height = left

    # Calculate final disorganization
    # Wall area = w * max_height
    # Chair area = total_chairs
    # Disorganization = wall_area - chair_area
    disorganization = w * max_height - total_chairs

    return disorganization


def demonstrate_algorithm(w, chair_counts):
    """Helper function to show step-by-step execution"""
    print(f"Room width: {w} meters")
    print(f"Chair counts by color: {chair_counts}")
    print(f"Total chairs: {sum(chair_counts)}")
    print()

    # Show binary search process
    left, right = 1, max(chair_counts)
    print("Binary search for minimum feasible max_height:")

    iteration = 1
    while left < right:
        mid = (left + right) // 2
        print(f"\nIteration {iteration}: left={left}, right={right}, mid={mid}")

        # Check feasibility
        stacks_needed = 0
        feasible = True

        print("  Stacks needed per color:")
        for i, count in enumerate(chair_counts):
            stacks_for_color = (count + mid - 1) // mid
            stacks_needed += stacks_for_color
            print(
                f"    Color {i+1} ({count} chairs): ceil({count}/{mid}) = {stacks_for_color} stacks"
            )

        print(f"  Total stacks needed: {stacks_needed}")
        print(f"  Available stacks: {w}")

        if stacks_needed <= w:
            print(f"  ✓ Feasible with max_height={mid}")
            right = mid
        else:
            print(f"  ✗ Not feasible, need max_height > {mid}")
            left = mid + 1

        iteration += 1

    final_height = left
    disorganization = w * final_height - sum(chair_counts)

    print(f"\nFinal result:")
    print(f"  Minimum max_height: {final_height}")
    print(f"  Wall area: {w} × {final_height} = {w * final_height}")
    print(f"  Chair area: {sum(chair_counts)}")
    print(
        f"  Disorganization: {w * final_height} - {sum(chair_counts)} = {disorganization}"
    )

    return disorganization


import sys


def main():
    lines = sys.stdin.read().strip().split("\n")
    n, w = map(int, lines[0].split())
    chair_counts = list(map(int, lines[1].split()))

    result = demonstrate_algorithm(w, chair_counts)
    print(result)


if __name__ == "__main__":
    main()
