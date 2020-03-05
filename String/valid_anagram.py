# Solution 1
# class Solution:
#     def isAnagram(self, s, t):
#         # return (len(s) == len(t) and sorted(s) == sorted(t))

# Solution 2
class Solution:
    def isAnagram(self, s, t):
        dict1, dict2 = {}, {}
        for each in s:
            dict1[each] = s.count(each)
        for each in t:
            dict2[each] = t.count(each)
        return dict1 == dict2

# Tests
s = Solution()
print(s.isAnagram("anagram", "nagaram"))  # True
print(s.isAnagram(["a", "b", "c"], ["c", "a", "b"]))  # True
print(s.isAnagram(["a", "b", "c"], ["c", "a", "v"]))  # False
