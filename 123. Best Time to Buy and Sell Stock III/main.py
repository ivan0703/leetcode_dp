from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        
        dp = [[0]*(len(prices)+1) for i in range(3)]
        for i in range(1,3):
            maxdiff = -math.inf
            for j in range(1,len(prices)+1):
                dp[i][j] = dp[i][j-1] # no transaction
                maxdiff = max(maxdiff, dp[i-1][j-1] - prices[j-1])
                dp[i][j] = max(dp[i][j], prices[j-1] + maxdiff)
        return dp[2][len(prices)]


if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4]
    sol = Solution()
    print('{0}'.format(sol.maxProfit(prices)))