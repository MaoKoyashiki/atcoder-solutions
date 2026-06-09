# EX12 - 最速のランナーを見つけよう https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_ck
N = int(input())  # 生徒の数Nを読み込む
T = list(map(int, input().split()))  # 各生徒のゴールまでの時間を読み込む
# ここにプログラムを追記
min_val = 10000000000000000000000
min_idx = 1
for i in range(N):
  if T[i] < min_val:
    min_val = T[i]
    min_idx = i + 1
    
print(min_idx)