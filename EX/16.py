# EX16 - 英単語テスト対策 https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_cg
N, K = map(int,input().split())
a = [word for word in input().split() if len(word) >= K]
print(*a)