# https://atcoder.jp/contests/arc029/tasks/arc029_1
n = int(input())
t = [int(input()) for i in range(n)]

ans = 10**9

for i in range(2**n):
    tmp = bin(i)[2:].zfill(n)
    a = []
    b = []
    for j in range(n):
        if tmp[j] == '0':
            a.append(t[j])
        else:
            b.append(t[j])
    ans = min(ans, max(sum(a), sum(b)))
print(ans)
