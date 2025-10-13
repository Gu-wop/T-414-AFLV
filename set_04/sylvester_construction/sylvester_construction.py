import sys


def hadamard_element(i, j, n):
    if n == 1:
        return 1

    half = n // 2
    # if i < 5:
    #     print(f"i={i}, j={j}, n={n}, half={half}")

    if i < half and j < half:
        return hadamard_element(i, j, half)
    elif i < half and j >= half:
        return hadamard_element(i, j - half, half)
    elif i >= half and j < half:
        return hadamard_element(i - half, j, half)
    else:
        return -hadamard_element(i - half, j - half, half)


def solve():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1

    for _ in range(t):
        n = int(data[idx])
        x = int(data[idx + 1])
        y = int(data[idx + 2])
        w = int(data[idx + 3])
        h = int(data[idx + 4])
        idx += 5

        for i in range(y, y + h):
            row = []
            for j in range(x, x + w):
                # print(f"i={i}, j={j}, n={n}")
                element = hadamard_element(i, j, n)
                print(f"element at ({i},{j}) = {element}")  # DEBUG
                row.append(str(element))

            sys.stdout.write(" ".join(row) + "\n")

        sys.stdout.write("\n")


if __name__ == "__main__":
    solve()
