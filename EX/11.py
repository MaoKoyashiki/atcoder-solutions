# EX11 - 足したり引いたり https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_cl
S = input()
a = list(S)
d = 1
i = 1
while i < len(a) - 1:
  if a[i] == "+":
    d += 1
  else:
    d -= 1
  i += 2
print(d)