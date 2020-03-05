class Solution:
    def findOcurrences(self, text, first, second):
        arr = text.split(" ")
        res = []
        for i in range(2, len(arr)):
            if arr[i - 2] == first and arr[i - 1] == second:
                res.append(arr[i])
        return res

# Tests
text = "one two three one two four five"
s = Solution()
print(s.findOcurrences(text, "one", "two"))  # ['three', 'four']
