class Solution:
    def minDays(self, n: int) -> int:
        """
        Given n oranges and three options for eating oranges
        each day, this program uses dynamic programming to determine
        the minimum number of days needed to eat the oranges.
        The three options are:
            - eat one orange
            - eat n/2 oranges if n is even multiple of 2
            - eat 2n/3 oranges if n is even multiple of 3

        :param n: number of oranges
        :type n: int
        :return: minimum days needed to eat n oranges
        :rtype: int
        """

        """
        Initialize:
        - Dynamic programming (dp_dict) maps number of oranges
          remaining to number of days elapsed. It is implemented
          as a hash table to accommodate large values of n. An
          array of size large n causes memory limit exceeded.
        - The queue contains the number of oranges remaining
          based on dynamic programming. It is initialized to
          a single entry of n.
        """
        dp_dict = {n: 0}
        queue = [n]

        """
        Dynamic Programming
        - Eat one orange per day until remaining oranges are
          a multiple of 2, then eat 1/2 of the oranges.
        - Eat one orange per day until remaining oranges are
          a multiple of 3, then eat 2/3 of the oranges.
        """
        while queue:
            num = queue.pop( 0 )
            new_num = num // 2
            if new_num:
                new_dp = dp_dict[num] + 1 + num % 2
            else:
                new_dp = dp_dict[num] + num % 2
            if new_num not in dp_dict or new_dp < dp_dict[new_num]:
                dp_dict[new_num] = new_dp
                if new_num and new_num not in queue:
                    queue.append( new_num )
            new_num = num // 3
            if new_num:
                new_dp = dp_dict[num] + 1 + num % 3
            else:
                new_dp = dp_dict[num] + num % 3
            if new_num not in dp_dict or new_dp < dp_dict[new_num]:
                dp_dict[new_num] = new_dp
                if new_num and new_num not in queue:
                    queue.append( new_num )
        return dp_dict[0]
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.minDays(10))
    print(sol.minDays(6))
    print(sol.minDays(1))
    print(sol.minDays(56))
    print(sol.minDays(9209408))
    print(sol.minDays(61455274))