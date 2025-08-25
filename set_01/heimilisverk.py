import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    try:
        n = int(data[0].strip())
    except ValueError:
        n = 0
    
    chores = data[1:]
    seen = set()
    out = []
    for chore in chores:
        if chore not in seen:
            seen.add(chore)
            out.append(chore)
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()