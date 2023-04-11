N = int(input()) # 사진개수
vote = int(input()) # 추천 회수
students = list(map(int, input().split())) # 추천 학생번호
picture = [];score = [] # 사진, 추천수

for i in range(vote):
    if students[i] in picture: # 사진에 있으면
        for j in range(len(picture)):
            if students[i] == picture[j]:
                score[j] += 1
    else: # 사진에 없으면
        if len(picture) >= N: # 사진 꽉차있으면
            for j in range(N):
                if score[j] == min(score): # 최소 점수
                    del picture[j];del score[j]
                    break # 찾으면 스탑 오래될수록 앞쪽
        picture.append(students[i]) # 새거 뒤에 더하기
        score.append(1)

picture.sort()
print(' '.join(map(str, picture)))