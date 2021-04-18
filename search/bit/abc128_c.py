# https://atcoder.jp/contests/abc128/tasks/abc128_c
n, m = map(int, input().split())
switch = [(i+1) for i in range(n)]
ks = [list(map(int, input().split())) for i in range(m)]
p = list(map(int, input().split()))
pattern = [bin(i)[2:].zfill(n) for i in range(2**n)]

ans = 0

for i in pattern:
    on = []
    light = 0
    for j in range(n):
        if i[j] == '1':
            on.append(switch[j])
    for k in range(m):
        count = 0
        for l in range(1, ks[k][0]+1):
            if ks[k][l] in on:
                count += 1
        if count % 2 == p[k]:
            light += 1
    if light == m:
        ans += 1

print(ans)
