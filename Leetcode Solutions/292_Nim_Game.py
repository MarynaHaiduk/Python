class Solution:
    def canWinNim(self, n):
        if n % 4 == 0:
            return False
        return True

# Tests
s = Solution()
print(s.canWinNim(16))  # False
print(s.canWinNim(2))   # True
