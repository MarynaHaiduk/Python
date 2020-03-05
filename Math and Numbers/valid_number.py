class Solution:
    def isNumber(self, s):
        try:
            float(s)
            return True
        except:
            return False

# Tests
s = Solution()
print(s.isNumber("0"))  # True
print(s.isNumber(" 0.1 "))  # True
print(s.isNumber("abc"))  # False
print(s.isNumber("1 a"))  # False
print(s.isNumber("2e10"))  # True
print(s.isNumber(" -90e3   "))  # True
print(s.isNumber(" 1e"))  # False
print(s.isNumber("e3"))  # False
print(s.isNumber(" 6e-1"))  # True
print(s.isNumber(" 99e2.5 "))  # False
print(s.isNumber("53.5e93"))  # True
print(s.isNumber(" --6 "))  # False
print(s.isNumber("-+3"))  # False
print(s.isNumber("95a54e53"))  # False
