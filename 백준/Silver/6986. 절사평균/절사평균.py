N, K = map(int, input().split())

score = []
for _ in range(N):
    score.append(float(input()) * 10) # 10곱해서 넣기 

score = sorted(score)[K:N-K] # 양끝 K개 자르기

trimmed_mean = 0 # 절사평균
for i in score:
    trimmed_mean += i
trimmed_mean = trimmed_mean / (N - 2 * K) / 10

adjusted_mean = 0 # 보정평균
for i in score:
    adjusted_mean += i
adjusted_mean = adjusted_mean + score[0] * K + score[-1] * K
adjusted_mean = adjusted_mean / N / 10

# 부동소수점 오류때무에 0.00000001 더해줘야됨
print("{:.2f}\n{:.2f}".format(trimmed_mean + 0.00000001, adjusted_mean + 0.00000001))
