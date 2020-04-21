from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dct = {}
        dp = [1] * len(arr)
        for i in range(len(arr)):
            diff = arr[i] - difference
            if diff in dct:
                dp[i] = dp[dct[diff]] + 1
            dct[arr[i]] = i
        return max(dp)

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubsequence([1,2,3,4], 1))
    print(sol.longestSubsequence([1,3,5,7], 1))
    print(sol.longestSubsequence([1,5,7,8,5,3,4,2,1], -2))