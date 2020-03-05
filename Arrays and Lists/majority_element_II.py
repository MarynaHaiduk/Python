class Solution:
    def majorityElement(self, nums):
        d = {}
        for i in set(nums):
            if i not in d and nums.count(i) > len(nums) // 3:
                d[i] = nums.count(i)
        return list(d.keys())

s = Solution()
print(s.majorityElement([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))  # [2]
