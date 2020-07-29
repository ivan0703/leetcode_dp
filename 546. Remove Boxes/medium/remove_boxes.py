class Solution:
    def rmSub(self, i, j, n, boxes, umap):
        '''
        Calculate the maximal points obtained from a subproblem (i,j,n)

        :param i: Start index of the continuous subarray
        :param j: End index of the continuous subarray
        :param n: Number of elements on the left
        :param boxes: Original box array
        :param umap: The dictionary stored previous sub-results 

        :returns: Maximal points of the subproblem
        '''
        if i > j:
            return 0
        
        # Check whether it's already solved
        if (i,j,n) in umap:
            return umap[(i,j,n)]

        # Remove consecutive same color in the left side
        while i < j and boxes[i+1] == boxes[i]:
            n += 1
            i += 1
        res = (n+1)**2 + self.rmSub(i+1,j,0,boxes,umap)

        # Combine the same-color box behind
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
        N = len(boxes)
        umap = dict()
        return self.rmSub(0, N-1, 0, boxes, umap)