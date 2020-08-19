from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        N = len(arr)

        # dp[i][j]: smallest sum of non-leaf nodes from arr[i:j+1] 
        dp = [[float('Inf') for _ in range(N)] for _ in range(N)]
        
        # max_elem[i][j]: max element within arr[i:j+1]
        max_elem = [[0 for _ in range(N)] for _ in range(N)]
        
        # initialization
        for i in range(N):
            dp[i][i] = 0
            max_elem[i][i] = arr[i]
        
        # Loop m in range(i,j)
        #   dp[i][m]: smallest sum of left childs
        #   dp[m+1][j]: smallest sum of right childs
        #   max_elem[i][m] * max_elem[m+1][j]: root node value
        for k in range(1,N):
            for i in range(0, N-k):
                j = i + k
                for m in range(i,j):
                    dp[i][j] = min(dp[i][j], 
                        dp[i][m] + dp[m+1][j] + max_elem[i][m] * max_elem[m+1][j])
                max_elem[i][j] = max(max_elem[i][j-1], arr[j])
        return dp[0][N-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.mctFromLeafValues([6,2,4]))