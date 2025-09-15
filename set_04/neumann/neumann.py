import sys


def neumann_recursive(n: int, sep=",") -> str:
    if n == 0:
        return "{}"

    arr = []
    for i in range(1, n + 1):
        if i == n:
            arr.append(neumann_recursive(n - 1, sep))
        else:
            arr.append("{" * i + "}" * i)
    output = "{" + sep.join(arr) + "}"
    return output


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    print(neumann_recursive(n))
