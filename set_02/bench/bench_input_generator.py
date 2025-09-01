# bench_input_generator.py
# Generates a deterministic benchmark input file named bench_input.txt

sizes = [1000]*10 + [10000]*10 + [100000]*10
T = len(sizes)

with open('bench_input.txt', 'w') as f:
    f.write(str(T) + "\n")
    for L in sizes:
        # deterministic repeating alphabet pattern
        s = ''.join(chr(ord('a') + (i % 26)) for i in range(L))
        f.write(s + "\n")

print('wrote bench_input.txt with', T, 'lines')
