from typing import List

class Solution:
    def rmSub(self, i, j, n, boxes, umap):
        '''
        Calculate the maximum points obtained from a subproblem (i,j,n)

        :param i: Start index of the continuous subarray
        :param j: End index of the continuous subarray
        :param n: Number of additional elements on the left
        :param boxes: Original box array
        :param umap: The dictionary stored previous sub-results 
        :returns: Maximum points of subproblem (i,j,n)
        '''
        # Empty array
        if i > j:
            return 0
        
        # Check whether it's already solved
        if (i,j,n) in umap:
            return umap[(i,j,n)]

        # Remove consecutive same-color boxes in the left side
        while i < j and boxes[i+1] == boxes[i]:
            n += 1
            i += 1
        res = (n+1)**2 + self.rmSub(i+1,j,0,boxes,umap)

        # Combine with a same-color box behind
        for k in range(i+1,j+1):
            if boxes[k] == boxes[i]:
                # Combine boxes[i] and its left n element with the continuous subarray boxes[k:j+1]
                res = max(res,
                    # subproblem (i+1,k-1,0) + subproblem (k,j,n+1)
                    self.rmSub(i+1,k-1,0,boxes,umap) + self.rmSub(k,j,n+1,boxes,umap))
        
        # Save the result of current subproblem
        umap[(i,j,n)] = res
        return res

    def removeBoxes(self, boxes: List[int]) -> int:
        '''
        Calculate the maximum points of the target array

        :param boxes: The box array contains positive numbers indicating 
                      different colors
        :returns: Maximum points of the target array
        '''
        N = len(boxes)
        umap = dict()
        # The original problem can be represented as a subproblem (0,N-1,0)
        return self.rmSub(0, N-1, 0, boxes, umap)


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeBoxes([1,3,1]))
    print(sol.removeBoxes([1,2,2,1,3,1]))
    print(sol.removeBoxes([1,3,2,2,2,3,4,3,1]))
    print(sol.removeBoxes([1,3,2,2,2,3]))

    ary = [3,8,8,5,5,3,9,2,4,4,6,5,8,4,8,6,9,6,2,8,6,4,1,9,5,3,10,5,3,3,9,8,8,6,5,3,7,4,9,6,3,9,4,3,5,10,7,6,10,7]
    print(sol.removeBoxes(ary))

    # 9606
    ary = [1,1,1,1,1,1,1,1,1,1,2,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print(sol.removeBoxes(ary))