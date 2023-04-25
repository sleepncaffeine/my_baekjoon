l, r = map(int, input().split())
res = 0

if len(str(l)) != len(str(r)):
    print(0)
else:
    sl = str(l)
    sr = str(r)
    for i in range(len(sl)):
        if sl[i] == sr[i]:
            if sl[i] == '8':
                res += 1
        else:
            break
    print(res)