from typing import List
from operator import itemgetter
import bisect

class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        h = len(startTime)
        jobs = []
        for i in range(h):
            jobs.append((startTime[i],endTime[i],profit[i]))
        # sort by endTime
        jobs.sort(key=itemgetter(1))
        ends = [x[1] for x in jobs]

        dp = [jobs[0][2]] + [0] * (h-1)
        for i in range(1,h):
            idx = bisect.bisect_right(ends, jobs[i][0], 0, i)
            pre = 0 if idx==0 else dp[idx-1]
            dp[i] = max(pre+jobs[i][2], dp[i-1])   

        return dp[-1]

if __name__ == "__main__":
    
    sol = Solution()

    startTime = [1,2,3,3]
    endTime = [3,4,5,6]
    profit = [50,10,40,70]
    print(sol.jobScheduling(startTime, endTime, profit))

    startTime = [1,2,3,4,6]
    endTime = [3,5,10,6,9]
    profit = [20,20,100,70,60]
    print(sol.jobScheduling(startTime, endTime, profit))

    startTime = [1,1,1]
    endTime = [2,3,4]
    profit = [5,6,4]
    print(sol.jobScheduling(startTime, endTime, profit))

    startTime = [6,15,7,11,1,3,16,2]
    endTime = [19,18,19,16,10,8,19,8]
    profit = [2,9,1,19,5,7,3,19]
    print(sol.jobScheduling(startTime, endTime, profit))