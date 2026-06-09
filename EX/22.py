# EX22 - 2つ目の値でソート https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_ca
N = int(input())
l = []
for i in range(N):
  t = tuple(map(int, input().split()))
  l.append(t)
l.sort(key = lambda x: x[1])
for i in l:
  print(*i)