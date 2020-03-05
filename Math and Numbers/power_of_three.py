class Solution:
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        if n < 3:
            return False
        while n != 3:
            if n % 3 == 0:
                n /= 3
            else:
                return False
        return True

# Tests
s = Solution()
print(s.isPowerOfThree(27))  # True
print(s.isPowerOfThree(45))  # False
