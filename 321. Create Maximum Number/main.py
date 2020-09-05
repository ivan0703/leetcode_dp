from typing import List

class Solution:
    def maxSingleK(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        m, M = 0, N - k
        ans = []
        for i in range(N):
            while ans and ans[-1] < nums[i] and m < M:
                m += 1
                ans.pop()
            if len(ans)==k:
                m += 1
            else:
                ans.append(nums[i])
        return ans

    def merge(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans.append(nums1[0])
                nums1.pop(0)
            else:
                ans.append(nums2[0])
                nums2.pop(0)
        return ans

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans = []
        start = max(0, k-len(nums2))
        end = min(k, len(nums1))
        for i in range(start, end+1):
            s1 = self.maxSingleK(nums1, i)
            s2 = self.maxSingleK(nums2, k-i)
            s = self.merge(s1,s2)
            ans = max(ans, s)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
    print(sol.maxNumber([6,7], [6,0,4], 5))
    print(sol.maxNumber([3,9], [8,9], 3))
    print(sol.maxNumber([5,6,8], [6,4,0], 3))
    
    # [4,3,1,6,5,4,7,3,9,5,3,7,8,4,1,3,5,9,1,1,4]
    print(sol.maxNumber([1,6,5,4,7,3,9,5,3,7,8,4,1,1,4],[4,3,1,3,5,9], 21))

    # [7,3,8,2,5,6,4,4,0,6,5,7,6,2,0]
    print(sol.maxNumber([2,5,6,4,4,0],[7,3,8,0,6,5,7,6,2], 15))

    print(sol.maxNumber([3,3,3,2,3,7,3,8,6,0,5,0,7,8,9,2,9,6,6,9,9,7,9,7,6,1,7,2,7,5,5,1],
        [5,6,4,9,6,9,2,2,7,5,4,3,0,0,1,7,1,8,1,5,2,5,7,0,4,3,8,7,3,8,5,3,8,3,4,0,2,3,8,2,7,1,2,3,8,7,6,7,1,1,3,9,0,5,2,8,2,8,7,5,0,8,0,7,2,8,5,6,5,9,5,1,5,2,6,2,4,9,9,7,6,5,7,9,2,8,8,3,5,9,5,1,8,8,4,6,6,3,8,4,6,6,1,3,4,1,6,7,0,8,0,3,3,1,8,2,2,4,5,7,3,7,7,4,3,7,3,0,7,3,0,9,7,6,0,3,0,3,1,5,1,4,5,2,7,6,2,4,2,9,5,5,9,8,4,2,3,6,1,9],
        160))