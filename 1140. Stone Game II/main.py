from typing import List
import math

class Solution:
    def maxPiles(self, m, i, rsum, dp):
        # already calculated
        if dp[m][i]>=0:
            return dp[m][i]

        # can take all remaining piles
        if i-1+2*m >= len(rsum)-1:
            dp[m][i] = rsum[i]
            return rsum[i]
        
        minOpponent = math.inf
        for x in range(2*m+1)[1:]:
            minOpponent = min(minOpponent, self.maxPiles(max(m,x),i+x,rsum,dp))
        
        dp[m][i] = rsum[i] - minOpponent
        return dp[m][i]

    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        dp = [[-1 for _ in range(N)] for _ in range(N+1)]
        rsum = piles.copy()
        for i in range(N)[N-2::-1]:
            rsum[i] += rsum[i+1]
        res = self.maxPiles(1,0,rsum,dp)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.stoneGameII([2,7,9,4,4]))