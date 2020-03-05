class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)

# Tests
s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))  # True
print(s.containsDuplicate([1, 2, 3, 4]))  # False
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
