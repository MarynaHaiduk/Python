class Solution:
    def largestUniqueNumber(self, A) -> int:
        res = [i for i in A if A.count(i) == 1]
        if res:
            return max(res)
        else:
            return -1

# Tests
s = Solution()
print(s.largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1])) # 8
print(s.largestUniqueNumber([99])) # 99
print(s.largestUniqueNumber([9, 9, 8, 8])) # -1
print(s.largestUniqueNumber([11, 10, 11])) # 10
