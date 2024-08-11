import sys


def dfs(idx):  # idx를 dfs 함수에 집어 넣는다.
    # visited를 계속 써야하기에, global 변수로 visited를 설정. 파이썬 파일 전체에 visited 전역변수를 설정.
    global visited
    visited[idx] = True  # 인덱스가 visited에 방문을 했다면, 다시는 들이지 마라.
    print(idx, end=' ')  # 현재 방문한 순서대로 계속해서 출력해주는데, 띄어쓰기로 공백을 넣어달라는 이야기.
    for next in range(1, N + 1):  # next라는 노드가 방문된 적이 없고, 내가 방문할 수 있는 곳이라면 방문을 하는 것. 따라서,
        # 만약에, 다음 노드가 방문된 적이 없다면, 그래프에서 idx에서 next가 있다면,
        if not visited[next] and graph[idx][next]:
            dfs(next)  # 그러면, 가겠다. 집어넣겠다!


def bfs():  # bfs() 함수는
    global q, visited  # q와 visited를 돌 것이다. (실행하는 파이썬 파일 전체 영역에서 사용 가능한 변수 설정)
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for next in range(1, N + 1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)


# 0. 입력 및 초기화
input = sys.stdin.readline
N, M, V = map(int, input().split())

# N + 1 by N + 1 의 false로 채워져 있는 2차원 행렬 (초기상태)
graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)  # 2차원 배열 하나의 칸에 들어가는 노드 (1차원 배열 하나)

# graph 정보 입력
for _ in range(M):  # M의 입력값을 집어 넣었을 때, 반복 작업을 할 것이다.
    a, b = map(int, input().split())  # a, b가 정수값으로 나타낼 것 이고, 문자열을 쪼갠다.
    graph[a][b] = True  # 만약 1, 2라는 정보가 주어지면 1에서 2로 갈 수 있고,
    graph[b][a] = True  # 2에서 1로도 갈 수 있다 라는 말

# 2. dfs
dfs(V)  # V라는 노드 부터 시작하겠다.
print()  # 출력해라.

# 3. bfs
visited = [False] * (N + 1)  # bfs 탐색할 땐, visited를 먼저 설정.
q = [V]  # q에 V 노드 부터, 탐색 할 것 이다.
visited[V] = True  # V 노드가 방문했다면, 다신 방문하지 않을 것이다.
bfs()  # bfs함수 출력
