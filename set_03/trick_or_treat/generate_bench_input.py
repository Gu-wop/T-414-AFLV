import random

def generate_test_case(n, coord_range=(-1000, 1000)):
    """Generate a test case with n houses."""
    lines = [str(n)]
    for _ in range(n):
        x = random.uniform(*coord_range)
        y = random.uniform(*coord_range)
        lines.append(f"{x:.6f} {y:.6f}")
    return "\n".join(lines)

# Generate multiple test cases
test_cases = [
    generate_test_case(10),    # Small case
    generate_test_case(100),   # Medium case
    generate_test_case(1000),  # Large case
    "0"  # End marker
]

with open('bench_input.txt', 'w') as f:
    f.write("\n".join(test_cases) + "\n")

print("Generated bench_input.txt with 3 test cases (n=10, 100, 1000) and end marker.")
