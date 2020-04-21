from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        elif len(nums) == 2:
            return 1 if nums[0]==nums[1] else 2
        
        dp_up   = [0] * len(nums)
        dp_down = [0] * len(nums)
        dp_up[0]   = 1
        dp_down[0] = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp_up[i] = max(dp_up[i], dp_down[j]+1)
                elif nums[i] < nums[j]:
                    dp_down[i] = max(dp_down[i], dp_up[j]+1)
        return max(dp_up + dp_down)

if __name__ == '__main__':
    nums1 = [1,7,4,9,2,5]
    nums2 = [1,17,5,10,13,15,10,5,16,8]
    nums3 = [0,0]
    
    sol = Solution()
    # print(sol.wiggleMaxLength(nums1))
    # print(sol.wiggleMaxLength(nums2))
    print(sol.wiggleMaxLength(nums3))
    