import sys
from math import gcd

input = sys.stdin.read

def solve():
  def check_num(n):
    if n == "0" or n == "1" or n == "2" or n == "3" or n == "4" or n == "5" or n == "6" or n == "7" or n == "8" or n == "9":
      return n
    else:
      return ""
    
  s = input()
  k = ""
  if not s:
      return
  for i in range(len(s)):
    t = check_num(s[i])
    k += t
  print(k)
  

if __name__ == "__main__":
  solve()

#################################################################
# 解説
import sys

def solve():
    # 入力をすべて受け取る
    s = sys.stdin.read()
    
    # 入力が空なら何もせず終了（元のコードの挙動を維持）
    if not s:
        return

    # 数字（'0'〜'9'）だけを抽出して一きに結合
    k = "".join(c for c in s if c in "0123456789")
    
    print(k)

if __name__ == "__main__":
    solve()