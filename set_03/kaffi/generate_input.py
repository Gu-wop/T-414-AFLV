import random

n = 1000000  # Number of chair types
w = 1000000  # Number of stacks
max_count = 1000000000  # Max chair count per type

with open('test_input.txt', 'w') as f:
    f.write(f"{n} {w}\n")
    chair_counts = [random.randint(1, max_count) for _ in range(n)]
    f.write(" ".join(map(str, chair_counts)) + "\n")

print("Generated test_input.txt")