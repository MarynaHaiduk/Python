class Solution:
    def findDuplicate(self, nums):
        arr = sorted(nums)
        for i in range(0, len(arr)-1):
            if arr[i] == arr[i + 1]:
                return arr[i]

# Tests
s = Solution()
print(s.findDuplicate([1, 3, 4, 2, 2]))  # 2
