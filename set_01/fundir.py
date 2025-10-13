import sys
import bisect
from collections import defaultdict


def is_conflict(intervals, t1, t2):
    i = bisect.bisect_right(intervals, (t1, t2))
    if i > 0:
        prev_start, prev_end = intervals[i - 1]
        if prev_end >= t1:
            return True
    if i < len(intervals):
        next_start, next_end = intervals[i]
        if next_start <= t2:
            return True
    return False


def insert_interval(intervals, t1, t2):
    bisect.insort(intervals, (t1, t2))


def main():
    input = sys.stdin.read
    data = input().split()

    q = int(data[0])
    index = 1

    meetings = defaultdict(list)
    print(meetings[1])
    print(meetings[2])
    results = []

    for _ in range(q):
        s = int(data[index])
        t1 = int(data[index + 1])
        t2 = int(data[index + 2])
        index += 3

        employee_meetings = meetings[s]
        if is_conflict(employee_meetings, t1, t2):
            results.append("Starfsmadur er thegar a fundi")
        else:
            insert_interval(employee_meetings, t1, t2)
            results.append("Fundur bokadur")

    print("\n".join(results))


if __name__ == "__main__":
    main()
