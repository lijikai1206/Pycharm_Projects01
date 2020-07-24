class Solution:
    def hammingWeight(self, n: int) -> int:
        num2 = bin(n)[2:]
        print(bin(n))
        print(num2)
        r = 0
        for i in range(len(num2)):
            if num2[i] == '1':
                r += 1
        return r

class Solution2:
    def hammingWeight(self, n: int) -> int:
        #位运算：减1相与
        count = 0
        while n:
            count += 1
            n = (n-1) & n
        return count

r = Solution().hammingWeight(5)
r2 = Solution2().hammingWeight(4)
print(r, r2)