import timeit
import subprocess
import sys

def run_script(script_name, input_file):
    """Run the script with input and capture output."""
    with open(input_file, 'r') as f:
        input_data = f.read()
    result = subprocess.run(
        [sys.executable, script_name],
        input=input_data,
        text=True,
        capture_output=True
    )
    return result.stdout.strip(), result.stderr.strip()

def benchmark(script_name, input_file, runs=5):
    """Benchmark a script using timeit for average time."""
    def timed_run():
        run_script(script_name, input_file)
    
    # Use timeit to measure execution time
    times = timeit.repeat(timed_run, repeat=runs, number=1)
    avg_time = sum(times) / len(times)
    return avg_time, times

if __name__ == "__main__":
    input_file = 'bench_input.txt'
    
    print("Benchmarking trick_or_treat.py...")
    avg_py, times_py = benchmark('trick_or_treat.py', input_file)
    print(f"Average time: {avg_py:.4f}s (runs: {times_py})")
    
    print("\nBenchmarking trick_or_treat_g.py...")
    avg_g, times_g = benchmark('trick_or_treat_g.py', input_file)
    print(f"Average time: {avg_g:.4f}s (runs: {times_g})")
    
    print(f"\nComparison: trick_or_treat_g.py is {avg_py / avg_g:.2f}x faster than trick_or_treat.py" if avg_g < avg_py else f"trick_or_treat.py is {avg_g / avg_py:.2f}x faster than trick_or_treat_g.py")
