class Solution:
    def minDays(self, n: int) -> int:
        dp = [0] + [float('Inf')] * n
        for i in range(n):
            dp[i+1] = min(dp[i+1], dp[i] + 1)
            if 2*i <= n:
                dp[2*i] = min(dp[2*i], dp[i]+1)
            if 3*i <= n:
                dp[3*i] = min(dp[3*i], dp[i]+1)
        return dp[n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.minDays(10))
    print(sol.minDays(6))
    print(sol.minDays(1))
    print(sol.minDays(56))
    print(sol.minDays(9209408))