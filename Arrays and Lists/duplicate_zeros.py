class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()
        print(arr)

# Tests
s = Solution()
print(s.duplicateZeros([1,0,2,3,0,4,5,0]))
# [1, 0, 0, 2, 3, 0, 0, 4]
