# Solution 1:
class Solution:
    def numJewelsInStones(self, J, S):
        count = 0
        if len(J) == 0 or len(S) == 0:
            return 0
        for stones in S:
            if stones in J:
                count += 1
        return count

# Solution 2:
# class Solution:
#     def numJewelsInStones(self, J, S):
#         return len([i for i in S if i in J])

# Tests
s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))  # 3
print(s.numJewelsInStones("z", "ZZ"))  # 0
