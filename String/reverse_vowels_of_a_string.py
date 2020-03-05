class Solution:
    def reverseVowels(self, s: str):
        tmp, res = [], ""
        for i in s:
            if i in "oeiuaOEIUA":
                tmp.append(i)
        for i in s:
            if i in "oeiuaOEIUA":
                res += tmp.pop()
            else:
                res += i
        return res

# Tests
s = Solution()
print(s.reverseVowels("hello"))  # holle
print(s.reverseVowels("leetcode"))  # leotcede
print(s.reverseVowels("aA"))  # Aa
