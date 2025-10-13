import sys


def main():
    string = sys.stdin.readline().strip()

    left = []
    right = []

    for char in string:

        if char == "L":
            print("appending right, popping left")
            right.append(left.pop())

        elif char == "R":
            print("appending left, popping right")
            left.append(right.pop())

        elif char == "B":
            print("backspace")
            left.pop()

        else:
            print("add: ", char)
            left.append(char)

        print("left: ", left)
        print("right: ", right)
        print()

    if right:
        left.extend(reversed(right))

    print("left: ", left)
    print("right: ", right)
    print()
    sys.stdout.write("".join(left))


if __name__ == "__main__":
    main()

    # arnarLLLBBun
