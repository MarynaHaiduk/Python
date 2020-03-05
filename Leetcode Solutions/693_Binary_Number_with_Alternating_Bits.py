class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num = bin(n)
        # alternating bits: two adjacent bits will always have different values
        # binary number start from 0b that is why start the iteration from 2
        for i in range(2, len(num) - 1):
            if num[i] == num[i+1]:
                return False
        return True

# Tests
s = Solution()
print(s.hasAlternatingBits(5))  # True
print(s.hasAlternatingBits(7))  # False
