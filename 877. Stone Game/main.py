from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[(0,0) for _ in range(len(piles))] for _ in range(len(piles))]
        
        for k in range(1, len(piles), 2):
            for i in range(0, len(piles)-k):
                j = i + k
                if k == 1:
                    if piles[i]>piles[j]:
                        dp[i][j] = (piles[i], piles[j])
                    else:
                        dp[i][j] = (piles[j],piles[i])
                else:
                    p1 = (dp[i][j-2][0] + piles[j], dp[i][j-2][1] + piles[j-1])
                    p2 = (dp[i+2][j][0] + piles[i], dp[i+2][j][1] + piles[i+1])
                    p3 = (dp[i+1][j-1][0] + max(piles[i],piles[j]), dp[i+1][j-1][1] + min(piles[i],piles[j]))
                    dp[i][j] = max(p1,p2,p3)
        return dp[0][len(piles)-1][0]>dp[0][len(piles)-1][1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.stoneGame([5,3,4,4,3,7]))