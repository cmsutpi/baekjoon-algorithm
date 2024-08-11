import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def dfs(x,y, farm):
    if farm[y][x] == 1:
        farm[y][x] = "w"


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    #Make a farm
    farm = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    for y in range(N):
        for x in range(M):
            if farm[y][x] == 1:
                dfs(x,y, farm)

