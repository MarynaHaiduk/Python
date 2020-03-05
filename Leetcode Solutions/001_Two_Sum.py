# Solution 1
# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(0, len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(0, len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[target - nums[i]] = i

# Tests
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  # [0,1]
print(s.twoSum([3,2,4], 6))  # [1,2]
