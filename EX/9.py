# EX9 - 電卓をつくろう2 https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_cn
N = int(input())
A = int(input())
for i in range(N):
  op, B = input().split()
  B = int(B)
  if op == "+":
      A += B
      print(i + 1, A)
  elif op == "-":
      A -= B
      print(i + 1, A)
  elif op == "*":
      A *= B
      print(i + 1, A)
  elif op == "/":
      if B != 0:
        A = A // B
        print(i + 1, A)
      else:
        print("error")
        break
  else:
    print("error")
    break
    