T = int(input())

for t in range(1, T + 1):
    n, p, q = map(int, input().split())
    eggs = list(map(int, input().split()))

    eggs.sort()
    total_weight = 0
    egg_count = 0

    for egg in eggs:
        if egg_count < p and total_weight + egg <= q:
            total_weight += egg
            egg_count += 1
        else:
            break

    print(f"Case {t}: {egg_count}")
