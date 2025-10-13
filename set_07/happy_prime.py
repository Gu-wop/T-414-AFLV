def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


P = int(input())
for _ in range(P):
    line = input().split()
    K = int(line[0])
    m = int(line[1])

    if is_prime(m) and is_happy(m):
        print(f"{K} {m} YES")
    else:
        print(f"{K} {m} NO")
