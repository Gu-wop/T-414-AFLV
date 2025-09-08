import sys
import math

def time_for_meeting_point(houses, mx):
    max_time = 0
    for x, y in houses:
        time = math.sqrt((x - mx)**2 + y**2)
        max_time = max(max_time, time)
    return max_time

def solve_case(houses):
    min_x = min(x for x, y in houses)
    max_x = max(x for x, y in houses)
    
    left = min_x - 1000
    right = max_x + 1000
    
    for _ in range(200):
        if right - left < 1e-12:
            break
            
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        
        if time_for_meeting_point(houses, m1) > time_for_meeting_point(houses, m2):
            left = m1
        else:
            right = m2
    
    optimal_x = (left + right) / 2
    optimal_time = time_for_meeting_point(houses, optimal_x)
    
    return optimal_x, optimal_time

def main():
    lines = sys.stdin.read().strip().split('\n')
    i = 0
    
    while i < len(lines):
        n = int(lines[i])
        i += 1
        
        if n == 0:
            break
            
        houses = []
        for j in range(n):
            x, y = map(float, lines[i + j].split())
            houses.append((x, y))
        i += n
        
        optimal_x, optimal_time = solve_case(houses)
        
        print(f"{optimal_x:.12f} {optimal_time:.12f}")
        
        i += 1

if __name__ == "__main__":
    main()