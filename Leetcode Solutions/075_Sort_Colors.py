class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # print(nums)

# Tests
s = Solution()
print(s.sortColors([2, 0, 2, 1, 1, 0]))  # [0, 0, 1, 1, 2, 2]
