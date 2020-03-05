class Solution:
    def findDuplicates(self, nums):
        arr = list(set(nums))
        for i in nums:
            if i in arr:
                arr.remove(i)
            else:
                arr.append(i)
        return arr

# Tests
s = Solution()
print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # [2, 3]
print(s.findDuplicates([9, 9, 4, 10, 8, 5, 2, 2, 7, 7]))  # [9, 2, 7]
