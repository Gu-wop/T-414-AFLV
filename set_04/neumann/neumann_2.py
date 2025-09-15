import sys


def neumann():
    n = int(sys.stdin.read().strip())
    if not input:
        return

    s = ["{}"]
    for i in range(1, n + 1):
        s.append("{" + ",".join(s[:i]) + "}")

    sys.stdout.write(s[n])


if __name__ == "__main__":
    neumann()
