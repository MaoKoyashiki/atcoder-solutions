# 配列の場合
import sys

def solve():
  lines = sys.stdin.read().split()
  if not lines:
    return

  # 数字に変換
  # N = int(lines[0])
  # A = lines[1:]
  A = list(map(int, A))


if __name__ == "__main__":
  solve()

# 1つの入力の場合
import sys

def solve():
  input_data = sys.stdin.read()
  if not input_data:
    return
  # 数字に変換
  N = int(input_data)


if __name__ == "__main__":
  solve()

# 行取得
import sys

def solve():
  input_data = sys.stdin.read().splitlines()
  
  if not input_data:
    return

  # 1行目の取得
  first_line = list(map(int, input_data[0].split()))
  N, M = first_line[0], first_line[1]

  # 外側でリストを定義
  all_rows = []

  # 2行目以降をループで回す
  for row_str in input_data[1:]:
    row = list(map(int, row_str.split()))
    # 定義したリストに追加していく
    all_rows.append(row)
  
  flag = False
  for i in range(N):
    p = all_rows[i][0]
    c = all_rows[i][1]
    s = all_rows[i][2:]
    for j in range(N):
      if i == j:
        continue
      p2 = all_rows[j][0]
      c2 = all_rows[j][1]
      s2 = all_rows[j][2:]   
      if p < p2 and set(s2).issubset(set(s)):
        flag = True
      elif p == p2 and set(s2).issubset(set(s)) and c > c2:
        flag = True
      else:
        continue
  if flag:
    print("Yes")
  else:
    print("No")
        
if __name__ == "__main__":
    solve()