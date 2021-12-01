from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * (N + 1)
        dp[1] = nums[0]
        for i in range(2, N+1):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
        return dp[N]

if __name__ == "__main__":
    sol = Solution()
    
    nums = [1,2,3,1]
    print(sol.rob(nums))

    nums = [2,7,9,3,1]
    print(sol.rob(nums))