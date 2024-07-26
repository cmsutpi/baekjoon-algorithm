# 다섯 줄의 입력을 받습니다.
words = [input().strip() for _ in range(5)]

# 최대 글자 수는 15
max_length = 15

# 세로로 읽은 결과를 저장할 리스트
result = []

# 최대 길이 15까지 각 열을 순회합니다.
for i in range(max_length):
    for word in words:
        if i < len(word):
            result.append(word[i])

# 결과를 공백 없이 출력합니다.
print(''.join(result))