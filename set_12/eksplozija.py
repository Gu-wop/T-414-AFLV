import sys

s = sys.stdin.readline().rstrip("\n")
bomb = sys.stdin.readline().rstrip("\n")

stack = []
m = len(bomb)
last = bomb[-1]

for ch in s:
    stack.append(ch)
    if ch == last and len(stack) >= m:
        if "".join(stack[-m:]) == bomb:
            del stack[-m:]

res = "".join(stack)
print(res if res else "FRULA")
