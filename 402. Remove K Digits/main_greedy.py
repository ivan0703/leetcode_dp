class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ret = []
        p, N = 0, len(num)
        for c in num:
            # To remove char from ret if
            #  1. Number of removed char is less than k
            #  2. ret is not empty and ret[-1] larger than c
            while p < k and ret and ret[-1] > c:
                ret.pop()
                p += 1
            
            # Check whether to append or remove current char c
            if len(ret) < N-k:
                ret.append(c)
            else:
                p += 1
        
        ret = "".join(ret).lstrip("0")
        return ret if ret else "0"


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeKdigits("1432219", 3))
    print(sol.removeKdigits("10200", 1))
    print(sol.removeKdigits("10", 2))
    print(sol.removeKdigits("9", 1))
    print(sol.removeKdigits("112", 1))
    