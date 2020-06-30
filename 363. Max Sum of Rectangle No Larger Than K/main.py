from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        M = len(matrix)
        N = len(matrix[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]

        for i in range(M):
            for j in range(N):
                a = matrix[i][j]
                if i > 0:
                    a += dp[i-1][j]
                if j > 0:
                    a += dp[i][j-1]
                if i > 0 and j > 0:
                    a -= dp[i-1][j-1]
                dp[i][j] = a

        ans = -float('Inf')
        for m in range(M):
            for n in range(N):
                for i in range(m+1):
                    for j in range(n+1):
                        a = dp[m][n]
                        if i > 0:
                            a -= dp[i-1][n]
                        if j > 0:
                            a -= dp[m][j-1]
                        if i > 0 and j > 0:
                            a += dp[i-1][j-1]
                        if a <= k:
                            ans = max(ans, a)
        return ans

if __name__ == "__main__":
    matrix = [[1,0,1],[0,-2,3]]
    k = 2
    
    sol = Solution()
    print(sol.maxSumSubmatrix(matrix,k))
    print(sol.maxSumSubmatrix([[2,2,-1]],0))
