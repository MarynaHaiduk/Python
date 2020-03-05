class Solution:
    def missingNumber(self, nums):
        return sum(list(range(0, len(nums) + 1))) - sum(nums)

# Tests
s = Solution()
print(s.missingNumber([3, 0, 1]))  # 2
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
