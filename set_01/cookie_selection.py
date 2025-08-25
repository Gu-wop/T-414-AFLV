import sys
import heapq

def main():
    lower = []
    upper = []
    out_lines = []

    def rebalance():
        if len(upper) < len(lower):
            heapq.heappush(upper, -heapq.heappop(lower))
        elif len(upper) > len(lower) + 1:
            heapq.heappush(lower, -heapq.heappop(upper))

    for i in sys.stdin.buffer.read().splitlines():
        if not i:
            continue
        s = i.strip()
        if s == b'#':
            val = heapq.heappop(upper)
            out_lines.append(str(val))
            rebalance()
        else:
            d = int(s)
            if not upper:
                heapq.heappush(upper, d)
            else:
                if d >= upper[0]:
                    heapq.heappush(upper, d)
                else:
                    heapq.heappush(lower, -d)
            rebalance()

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
