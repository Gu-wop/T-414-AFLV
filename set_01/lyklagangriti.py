import sys

def main():
    string = sys.stdin.readline().strip()

    left = []
    right = []

    for char in string:
        if char == 'L':
            right.append(left.pop())
        elif char == 'R':
            left.append(right.pop())
        elif char == 'B':
            left.pop()
        else:
            left.append(char)

    if right:
        left.extend(reversed(right))
    sys.stdout.write(''.join(left))

if __name__ == "__main__":
    main()
