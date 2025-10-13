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


def standard_von_neumann(n):
    if n == 0:
        return "{}"

    elements = []
    for i in range(n):  # Loop from 0 to n-1
        elements.append(standard_von_neumann(i))

    return "{" + ",".join(elements) + "}"


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    print(standard_von_neumann(n))
    print()
    # print(neumann_recursive(n))
