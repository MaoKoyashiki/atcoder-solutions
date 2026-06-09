# EX20 - 最頻値 https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_cc
N = int(input()) 
l = [int(x) for x in input().split()]
counter = {}
 
for x in l:
  # counter に要素 x が存在しない状態で counter[x] += 1 とするとエラーになるので、
  # if 文で判定し、あらかじめ代入しておく
  if x not in counter:
    counter[x] = 0
  counter[x] += 1
idx = -1
cnt = 0 
for k, v in counter.items():
  if v > cnt:
    cnt = v
    idx = k
print(idx, cnt)