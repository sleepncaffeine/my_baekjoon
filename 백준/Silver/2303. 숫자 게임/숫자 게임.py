score = []
n = int(input())
for i in range(n):
  card = list(map(int, input().split()))
  max_digit = 0 # 최대 일의자리수
  for i in range(5):
    for j in range(i + 1, 5):
      for k in range(j + 1, 5):
        digit = (card[i] + card[j] + card[k]) % 10 # 일의자리수
        max_digit = max(max_digit, digit)
  score.append(max_digit)

for i in range(n - 1, -1, -1): # 번호최대 사람 번호
  if score[i] == max(score): # 최고 점수
    print(i + 1)
    break