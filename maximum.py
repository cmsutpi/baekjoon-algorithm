# 9x9 격자판을 입력받고, 최댓값과 위치를 찾는 프로그램

# 격자판 입력 받기
matrix = []
for _ in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)

# 최댓값 및 위치 초기화
max_value = -1
max_row = -1
max_col = -1

# 격자판 순회하면서 최댓값 찾기
for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row = i + 1  # 1행 1열 기준이므로 인덱스에 +1
            max_col = j + 1  # 1행 1열 기준이므로 인덱스에 +1

# 최댓값과 위치 출력
print(max_value)
print(max_row, max_col)