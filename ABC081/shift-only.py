a = [1, 2, 4, 5, 11]
N = len(a)
flag = True
def solve():
	count = 0
	while flag:
		for j in range(len(a)):
			if a[j] % 2 == 0:
				a[j] = a[j] // 2
			else:
				flag = False
				break
		count += 1
	return count

if __name__ == "__main__":
	print(solve())
