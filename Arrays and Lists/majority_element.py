class Solution:
    def majorityElement(self, nums):
        for i in set(nums):
            if nums.count(i) > len(nums) // 2:
                return i

# Tests
s = Solution()
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
