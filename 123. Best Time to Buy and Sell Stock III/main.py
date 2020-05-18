from typing import List
import math

class Solution:
    def maxProfit_dp(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        
        dp = [[0]*(len(prices)+1) for i in range(3)]
        for i in range(1,3):
            maxdiff = -math.inf
            for j in range(1,len(prices)+1):
                dp[i][j] = dp[i][j-1] # no transaction
                maxdiff = max(maxdiff, dp[i-1][j-1] - prices[j-1]) # buy2
                dp[i][j] = max(dp[i][j], prices[j-1] + maxdiff)
        return dp[2][len(prices)]
    
    def maxProfit(self, prices: List[int]) -> int:
        first_buy   = -math.inf
        first_sell  = 0
        second_buy  = -math.inf
        second_sell = 0
        for i in range(len(prices)):
            first_buy = max(first_buy, -prices[i])
            first_sell = max(first_sell, first_buy+prices[i])
            second_buy = max(second_buy, first_sell-prices[i])
            second_sell = max(second_sell, second_buy+prices[i])
        return second_sell
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([3,3,5,0,0,3,1,4]))
    print(sol.maxProfit([1,2,3,4,5]))
    print(sol.maxProfit([5,4,3,2,1]))