from typing import List, Dict

class Solution:
    def getColor(self, start: int, subList: List[int]):
        if start >= len(subList):
            return 0, len(subList)
        cnt, nxt = 1, start+1
        c = subList[start]
        while nxt < len(subList) and c==subList[nxt]:
            nxt += 1
            cnt += 1
        return cnt, nxt

    def maxPoint(self, subList: List[int], umap: Dict[str,int]):
        if not subList:
            return 0
        
        key = "".join([str(n) + "," for n in subList])
        if key in umap:
            return umap[key]

        start, ans = 0, 0
        while True:
            cnt, nxt = self.getColor(start, subList)
            if cnt == 0:
                break
            ary = subList[0:start] + subList[start+cnt:]
            ans = max(ans, cnt*cnt + self.maxPoint(ary,umap))
            start = nxt
        umap[key] = ans
        
        return ans

    def removeBoxes(self, boxes: List[int]) -> int:
        umap = dict()
        return self.maxPoint(boxes, umap)

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeBoxes([1,3,2,2,2,3,4,3,1]))
    print(sol.removeBoxes([1,3,2,2,2,3]))

    # ary = [3,8,8,5,5,3,9,2,4,4,6,5,8,4,8,6,9,6,2,8,6,4,1,9,5,3,10,5,3,3,9,8,8,6,5,3,7,4,9,6,3,9,4,3,5,10,7,6,10,7]
    ary = [3,8,8,5,5,3,9,2,4,4,6,5,8,4,8,6,9,6,2]
    print(sol.removeBoxes(ary))