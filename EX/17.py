# EX17 - ゲーム大会 https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_cf
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(M)]

# ここにコードを追記する
a = [["-" for _ in range(N)] for _ in range(N)]

for x in AB:
  a[x[0] - 1][x[1] - 1] = "o"
  a[x[1] - 1][x[0] - 1] = "x"
  
for x in a:
  print(*x)