from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)
        res = 1

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
        return res

    def lengthOfLISv2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = []
        for i in range(len(nums)):
            p = bisect.bisect_left(res, nums[i])
            if p == len(res):
                res.append(nums[i])
            else:
                res[p] = nums[i]
        return len(res)

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(sol.lengthOfLISv2([10,9,2,5,3,7,101,18]))