from typing import List

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if len(A)==0 or len(A)!=len(B):
            return False
        
        res = 0
        N = len(A)
        dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
        for i in range(1,N+1):
            for j in range(1,N+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.findLength([1,2,3,2,1],[3,2,1,4,7]))
