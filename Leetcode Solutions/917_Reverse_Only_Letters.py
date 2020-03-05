class Solution:
    def reverseOnlyLetters(self, S):
        arr= []
        res = ""
        for i in S:
            if i.isalpha():
                arr.append(i)
        for i in S:
            if i.isalpha():
                res += arr.pop()
            else:
                res += i
        return res

# Tests
s = Solution()
print(s.reverseOnlyLetters("ab-cd"))  # dc-ba
print(s.reverseOnlyLetters("a-bC-dEf-ghIj"))  # j-Ih-gfE-dCba
print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # Qedo1ct-eeLg=ntse-T!
