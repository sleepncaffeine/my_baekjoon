import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
checks = list(map(int, input().split()))

for c in checks:
    l, h = 0, N - 1
    exist = False
    
    while l <= h:
        m = (l + h) // 2
        if cards[m] > c:
            h = m - 1
        elif cards[m] < c:
            l = m + 1
        else:
            exist = True
            break
            
    print(1 if exist else 0, end=' ')