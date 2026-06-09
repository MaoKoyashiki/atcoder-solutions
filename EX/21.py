# EX21 - Bitwise Exclusive Or https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_cb
a, b = map(int, input().split())

# x = 13 # 2進法で 1101
# print((x >> 0) & 1) # 1
# print((x >> 1) & 1) # 0
# print((x >> 2) & 1) # 1
# print((x >> 3) & 1) # 1
# print((x >> 4) & 1) # 0
# print((x >> 5) & 1) # 0

# if a >> 0 == 1 & b >> 0 == 1:
#   c == 0
# if a >> 0 == 1 & b >> 0 == 0:
#   c == 1
# if a >> 0 == 0 & b >> 0 == 1:
#   c == 1
# if a >> 0 == 0 & b >> 0 == 0:
#   c == 0
print(a ^ b)