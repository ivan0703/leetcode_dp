class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i][j]: number of BST formed by [i,...,j]
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for k in range(1,n):
            for i in range(0,n-k):
                j = i + k
                # [i,...,m-1] + [m] + [m+1,...,j]
                for m in range(i, j+1):
                    left  = dp[i][m-1] if m - 1 >= i else 1
                    right = dp[m+1][j] if m + 1 <= j else 1
                    dp[i][j] += left * right
        return dp[0][n-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.numTrees(3))