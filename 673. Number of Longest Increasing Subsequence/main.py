from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        cnt = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    if(dp[i]<dp[j]+1):
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif(dp[i]==dp[j]+1):
                        cnt[i] = cnt[i] + cnt[j]
        idx = [i for i,j in enumerate(dp) if j==max(dp)]
        return sum([cnt[i] for i in idx])

if __name__ == '__main__':
    sol = Solution()
    print(sol.findNumberOfLIS([1,3,5,4,7]))       # 2
    print(sol.findNumberOfLIS([2,2,2,2,2]))       # 5
    print(sol.findNumberOfLIS([1,2,4,3,5,4,7,2])) # 3