# 計算量: O(N * 2^N)
# ポイントはbit全探索で部分集合を全て列挙することです。
# これはO(2^N)で列挙できます。
# その後、部分集合の和を計算して、Wと一致するかどうかを判定します。
# これはO(N)で計算できます。
# したがって、計算量はO(N * 2^N)です。
N = 5
W = 10
a = [1, 2, 4, 5, 11]

flag = False
def solve():
	for i in range(1 << N): #2^N
		sum = 0
		for j in range(N): # N
			if i & (1 << j):
				sum += a[j]
		if sum == w:
			flag = True
			return True
	return False


if __name__ == "__main__":
    if solve():
		print("Yes")
	else:
		print("No")