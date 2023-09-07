s, p = map(int, input().split())
arr = list(input())
check = list(map(int, input().split()))
current = [0] * 4  # a, c, g, t

ans = 0

for i in range(s - p + 1):
    if i == 0:
        for j in range(p):
            if arr[j] == "A":
                current[0] += 1
            elif arr[j] == "C":
                current[1] += 1
            elif arr[j] == "G":
                current[2] += 1
            else:
                current[3] += 1
    else:
        if arr[i - 1] == "A":
            current[0] -= 1
        elif arr[i - 1] == "C":
            current[1] -= 1
        elif arr[i - 1] == "G":
            current[2] -= 1
        else:
            current[3] -= 1
            
        if arr[i + p - 1] == "A":
            current[0] += 1
        elif arr[i + p - 1] == "C":
            current[1] += 1
        elif arr[i + p - 1] == "G":
            current[2] += 1
        else:
            current[3] += 1

    if (
        current[0] >= check[0]
        and current[1] >= check[1]
        and current[2] >= check[2]
        and current[3] >= check[3]
    ):
        ans += 1

print(ans)