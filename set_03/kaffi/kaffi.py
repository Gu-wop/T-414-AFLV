import math


def can_fit_with_max_height(max_height, chair_counts, w):
    stacks_needed = 0

    print(f"\nChecking max_height: {max_height}")
    print(chair_counts)

    for count in chair_counts:
        stacks_needed += (count + max_height - 1) // max_height
        stacks_needed += math.ceil(count / max_height)

        print(
            f"Count: {count}, Max Height: {max_height}, Stacks Needed: {stacks_needed}"
        )
        if stacks_needed > w:
            print("Exceeded width limit")
            return False

    return stacks_needed <= w


def solve_chair_stacking(w, chair_counts):
    total_chairs = sum(chair_counts)

    left, right = 1, max(chair_counts)

    while left < right:
        mid = (left + right) // 2
        if can_fit_with_max_height(mid, chair_counts, w):
            right = mid
        else:
            left = mid + 1

    max_height = left
    disorganization = w * max_height - total_chairs

    return disorganization


import sys


def main():
    lines = sys.stdin.read().strip().split("\n")
    n, w = map(int, lines[0].split())
    chair_counts = list(map(int, lines[1].split()))

    result = solve_chair_stacking(w, chair_counts)
    print(result)


if __name__ == "__main__":
    main()
