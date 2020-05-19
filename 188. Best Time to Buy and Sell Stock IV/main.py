from typing import List
import math

class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        
        if N <= 2 and k < 1:
            return 0

        # k >= N//2
        if k >= N//2:
            profit = 0
            for i in range(1,N):
                profit += max(0, prices[i]-prices[i-1])
            return profit

        dp = [[0 for _ in range(len(prices)+1)] for _ in range(2)]
        for i in range(1,k+1):
            max_sell = -math.inf
            for j in range(1,len(prices)+1):
                max_sell = max(max_sell, dp[(i-1)%2][j-1]-prices[j-1])
                dp[i%2][j] = max(dp[i%2][j-1], max_sell+prices[j-1])
        return dp[k%2][len(prices)]

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(2,[2,4,1]))
    print(sol.maxProfit(2,[3,2,6,5,0,3]))
    print(sol.maxProfit(2,[3,3,5,0,0,3,1,4]))
    print(sol.maxProfit(10,[3,2,6,5,0,3]))