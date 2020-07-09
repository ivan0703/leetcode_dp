from typing import List
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        M, N = len(matrix), len(matrix[0])
        ans = -float('Inf')
        for n in range(N):
            csum = [0] * M
            for j in range(n, N):
                for i in range(M):
                    csum[i] += matrix[i][j]
                ans = max(ans, self.maxSumSubarray(csum, k))

        return ans

    def maxSumSubarray(self, array: List[int], k: int) -> int:
        if len(array) == 0:
            return 0
        
        ans, psum = -float('Inf'), 0
        sumary = [0]
        for i in range(len(array)):
            psum += array[i]
            idx = bisect.bisect_right(sumary, psum - k)
            if idx > 0 and sumary[idx-1] == psum - k:
                return k
            elif idx < len(sumary):
                ans = max(ans, psum-sumary[idx])
            idx = bisect.bisect_left(sumary, psum)
            if idx < len(sumary) and sumary[idx] == psum:
                continue
            sumary.insert(idx, psum)
        return ans

if __name__ == "__main__":
    matrix = [[1,0,1],[0,-2,3]]
    k = 2
    
    sol = Solution()
    # print(sol.maxSumSubmatrix(matrix,k))
    print(sol.maxSumSubmatrix([[2,2,-1]],0))
    # print(sol.maxSumSubmatrix([[2,2,-1]],3))
