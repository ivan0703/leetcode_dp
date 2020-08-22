class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(n+1)]
        for k in range(1,n):
            for i in range(1,n+1-k):
                j = i + k
                dp[i][j] = float('Inf')
                for m in range(i,j+1):
                    left  = dp[i][m-1] if m > i else 0
                    right = dp[m+1][j] if m < j else 0
                    dp[i][j] = min(dp[i][j], m + max(left, right))
        return dp[1][n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.getMoneyAmount(2))
    print(sol.getMoneyAmount(10))