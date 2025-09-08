def solve_chair_stacking(w, chair_counts):
    total_chairs = sum(chair_counts)
    
    left, right = 1, max(chair_counts)
    
    def can_fit_with_max_height(max_height):
        stacks_needed = 0
        
        for count in chair_counts:
            stacks_needed += (count + max_height - 1) // max_height
            if stacks_needed > w:
                return False
        
        return stacks_needed <= w
    
    while left < right:
        mid = (left + right) // 2
        if can_fit_with_max_height(mid):
            right = mid
        else:
            left = mid + 1
    
    max_height = left
    disorganization = w * max_height - total_chairs
    
    return disorganization

import sys

def main():
    lines = sys.stdin.read().strip().split('\n')
    n, w = map(int, lines[0].split())
    chair_counts = list(map(int, lines[1].split()))
    
    result = solve_chair_stacking(w, chair_counts)
    print(result)

if __name__ == "__main__":
    main()