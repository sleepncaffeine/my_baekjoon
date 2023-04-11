def find_clock_num(x):
    clock_num = x
    for _ in range(3):
        x = (x % 1000) * 10 + x // 1000
        if clock_num > x:
            clock_num = x
    return clock_num

clock_num = find_clock_num(int(''.join(input().split()))) # 2 1 1 2 -> 2112

i = 1111
cnt = 0
while(i <= clock_num): # 1111부터 시계수까지 개수세기
    if find_clock_num(i) == i:
        cnt += 1
    i += 1
print(cnt)
