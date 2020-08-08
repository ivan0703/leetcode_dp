from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        # Create an intervals list, each of which is the water range of 
        # a certain tap. Sort them according to their left ends. 
        intr = []
        for i in range(len(ranges)):
            if ranges[i] == 0:
                continue
            intr.append((i-ranges[i], i+ranges[i]))
        intr.sort(key=lambda x: x[0])

        # No interval available or 0 is not covered
        if len(intr) == 0 or intr[0][0] > 0:
            return -1

        cnt = 1
        left, right = 0, intr[0][1]
        for i in range(1,len(intr)):
            # The left end of interval-i is larger than current
            # right-most end.
            if intr[i][0] > right:
                return -1
            
            if intr[i][0] <= left:
                # Find the right-most point among the intervals which
                # cover the 'left' point
                right = max(right, intr[i][1])
            elif intr[i][1] > right:
                # Next segment:
                # 'left' is updated to previous 'right'
                # 'right' is updated to interval-i's right end
                cnt += 1
                left = right
                right = intr[i][1]

            # Whenever 'n' is covered, stop
            if right >= n:
                return cnt    

        # Loop through all the intervals, but 'n' couldn't be covered
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.minTaps(5, [3,4,1,1,0,0])) # 1
    print(sol.minTaps(3, [0,0,0,0])) # -1
    print(sol.minTaps(7, [1,2,1,0,2,1,0,1])) # 3
    print(sol.minTaps(8, [4,0,0,0,0,0,0,0,4])) # 2
    print(sol.minTaps(8, [4,0,0,0,4,0,0,0,4])) # 1