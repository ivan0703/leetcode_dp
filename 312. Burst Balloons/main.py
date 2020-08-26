from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[0]*(N+2) for _ in range(N+2)]
        nums.insert(0,1)
        nums.append(1)

        for i in range(1,N+1):
            dp[i][i] = nums[i-1] * nums[i] * nums[i+1]
        
        for k in range(1,N):
            for i in range(1, N+1-k):
                j = i + k
                dp[i][j] = -float('Inf')
                for m in range(i,j+1):
                    dp[i][j] = max(dp[i][j], nums[i-1]*nums[m]*nums[j+1] + dp[i][m-1] + dp[m+1][j])
        return dp[1][N]

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxCoins([3,1,5,8]))