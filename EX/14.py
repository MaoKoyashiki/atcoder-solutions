# EX14 - 隣り合う同じ値を探す https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_ci
data = [int(c) for c in input().split()]
# dataの中で隣り合う等しい要素が存在するなら"YES"を出力し、そうでなければ"NO"を出力する
# ここにプログラムを追記
isExist = False

tmp = "start!"
for i in range(len(data)):
  if i == 0:
    tmp = data[i]
    continue
  
  if data[i] == tmp:
    isExist = True
    break
  
  tmp = data[i]
  
if isExist:
  print("YES")
else:
  print("NO")