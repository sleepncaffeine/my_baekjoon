N = int(input())
num = list(map(int, input().split()))
num.sort()

if (N % 2) == 0: # 짝수, 가운데 값 중 작은값
    print(num[N // 2 - 1])
else: # 홀수, 가운데 값
    print(num[N // 2])