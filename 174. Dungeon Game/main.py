from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M = len(dungeon)
        N = len(dungeon[0])
        dp = [[float('Inf') for _ in range(N) ] for _ in range(M)]

        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                if i == M-1 and j == N-1:
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                    continue
                if i < M-1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j] - dungeon[i][j])
                if j < N-1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] - dungeon[i][j])
                dp[i][j] = max(1, dp[i][j])

        return dp[0][0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.calculateMinimumHP([[100]]) )
    print(sol.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]) )
    print(sol.calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]]) )