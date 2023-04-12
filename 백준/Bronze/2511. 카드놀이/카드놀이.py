A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A == B:
    print(10, 10); 
    print("D")
else:
    a_score = b_score = 0
    for i in range(10):
        if A[i] > B[i]:
            a_score += 3
            win = 'A'
        elif A[i] < B[i]:
            b_score += 3
            win = 'B'
        else:
            a_score += 1
            b_score += 1;    
    print(a_score, b_score)
    if a_score == b_score:
        print(win)
    else:
        print('A' if a_score > b_score else 'B')