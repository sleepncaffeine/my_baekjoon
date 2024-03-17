import sys

input = sys.stdin.readline

n, m = map(int, input().split())
words = dict()
for _ in range(n):
    wd = input().strip()
    
    if len(wd) < m:
        continue

    if words.get(wd):
        words[wd][0] += 1
    else:
        words[wd] = [1, len(wd), wd]

words = sorted(words.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))
# print()
for w, c in words:
    print(w)