
# 深さ優先探索（行きがけ）
from collections import deque
import sys
input = sys.stdin.readline

# グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
    u, k, * v = [int(x) for x in input().split()]  # uは頂点番号、kは隣接頂点の個数
    v.sort()
    for i in v:
        graph[u].append(i)
        # graph[i].append(u) # 無向グラフ

time = 0
arrive_time = [-1] * (N + 1)  # 到着時刻

# 深さ優先探索


def dfs(v):
    global time
    time += 1
    stack = [v]
    arrive_time[v] = time
    while stack:
        v = stack[-1]
        if graph[v]:
            w = graph[v].popleft()
            if arrive_time[w] < 0:
                time += 1
                arrive_time[w] = time
                stack.append(w)
        else:
            stack.pop()
    return arrive_time


# 孤立している頂点対策
for i in range(N):
    if arrive_time[i + 1] < 0:
        ans = dfs(i + 1)

# 頂点番号、到着時刻
for j in range(N):
    temp = [j + 1, ans[j + 1]]
    print(* temp)
