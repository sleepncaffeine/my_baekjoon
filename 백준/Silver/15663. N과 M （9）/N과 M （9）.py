from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

permutation = set(permutations(numbers, M))

permutation = sorted(permutation)

for p in permutation:
    print(" ".join(map(str, p)))
