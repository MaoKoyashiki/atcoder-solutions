K = 7
N = 10
def solve():
    count = 0
    for i in range(1, K + 1):
        for j in range(1, K + 1):
            k = N - (i + j)
            if 1 <= k <= K:
                count += 1
    return count

if __name__ == "__main__":
    print(solve())