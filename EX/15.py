# EX15 - 果物屋さんでお買い物 https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_ch
N, S = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
# ここにプログラムを追記
cnt = 0

for i in range(N):
  for j in range(N):
    if A[i] + B[j] == S:
      cnt += 1
      
print(cnt)