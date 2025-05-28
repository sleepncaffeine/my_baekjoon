import sys

for line in sys.stdin:
    if not line.strip():
        break

    a = list(map(int, line.strip().split()))
    n, seq = a[0], a[1:]

    if n == 1:
        print("Jolly")
        continue

    diffs = set(abs(seq[i] - seq[i + 1]) for i in range(n - 1))

    if diffs == set(range(1, n)):
        print("Jolly")
    else:
        print("Not jolly")
