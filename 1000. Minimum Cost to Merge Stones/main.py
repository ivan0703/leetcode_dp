from typing import List

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        N = len(stones)
        if (N-1) % (K-1) != 0:
            return -1

        dp = [[0 for _ in range(N)] for _ in range(N)]
        sum = [stones[0]] + [0] * (N-1)
        for i in range(1,N):
            sum[i] = stones[i] + sum[i-1]
        for n in range(K-1, N):
            for i in range(N-n):
                j = i + n
                dp[i][j] = float('Inf')
                for m in range(i,j,K-1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m+1][j])
                if (j-i)%(K-1) == 0:
                    dp[i][j] += sum[j] - (sum[i-1] if i > 0 else 0)
        return dp[0][N-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeStones([3,2,4,1], 2))
    print(sol.mergeStones([3,2,4,1], 3))
    print(sol.mergeStones([3,5,1,2,6], 3))