from typing import List

class Solution:    
    def minScoreTriangulation(self, A: List[int]) -> int:
        N = len(A)
        dp = [[float('Inf')] * N for _ in range(N)]
        for k in range(2,N):
            for i in range(N-k):
                j = i + k
                for m in range(i+1, j):
                    left  = dp[i][m] if m - i >= 2 else 0
                    right = dp[m][j] if j - m >= 2 else 0
                    dp[i][j] = min(dp[i][j], left + A[i]*A[j]*A[m] + right)
        return dp[0][N-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.minScoreTriangulation([1,2,3]))
    print(sol.minScoreTriangulation([3,7,4,5]))
    print(sol.minScoreTriangulation([1,3,1,4,1,5]))