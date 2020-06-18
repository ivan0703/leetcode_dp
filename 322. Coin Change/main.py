from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        dp = [float('inf')] * amount + [0]
        res = 0
        while True:
            update = False
            for i in range(N):
                for j in range(len(dp)):
                    if dp[j] == res and j - coins[i] >= 0:
                        if dp[j-coins[i]]==float('inf'):
                            dp[j-coins[i]] = res + 1
                        update = True

            if dp[0] != float('inf'):
                return dp[0]
            elif not update:
                return -1
            else:
                res += 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    # print(sol.coinChange([1, 2, 5], 11))
    # print(sol.coinChange([2], 3))
    print(sol.coinChange([1, 2, 5, 10], 27))