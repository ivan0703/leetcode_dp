from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        #         
        intr = []
        for i in range(len(ranges)):
            if ranges[i] == 0:
                continue
            intr.append((i-ranges[i], i+ranges[i]))
        intr.sort(key=lambda x: x[0])

        if len(intr) == 0 or intr[0][0] > 0:
            return -1

        cnt = 1
        left, right = 0, intr[0][1]
        for i in range(1,len(intr)):
            if intr[i][0] > right:
                return -1
            
            if intr[i][0] <= left:
                right = max(right, intr[i][1])
            elif intr[i][1] > right:
                cnt += 1
                left = right
                right = max(left, intr[i][1])  

            if right >= n:
                return cnt    

        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.minTaps(5, [3,4,1,1,0,0])) # 1
    print(sol.minTaps(3, [0,0,0,0])) # -1
    print(sol.minTaps(7, [1,2,1,0,2,1,0,1])) # 3
    print(sol.minTaps(8, [4,0,0,0,0,0,0,0,4])) # 2
    print(sol.minTaps(8, [4,0,0,0,4,0,0,0,4])) # 1