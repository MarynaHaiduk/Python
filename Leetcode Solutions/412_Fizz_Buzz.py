# Solution 1
# class Solution:
#     def fizzBuzz(self, n):
#         arr = []
#         for i in range(1, n + 1):
#             s = ''
#             if i % 3 == 0:
#                 s += "Fizz"
#             if i % 5 == 0:
#                 s += "Buzz"
#             if s == '':
#                 s += str(i)
#             arr.append(s)
#         return arr

# Solution 2
class Solution:
    def fizzBuzz(self, n):
        arr = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                arr.append('FizzBuzz')
            elif i % 5 == 0:
                arr.append('Buzz')
            elif i % 3 == 0:
                arr.append('Fizz')
            else:
                arr.append(str(i))
        return arr

# Tests
s = Solution()
print(s.fizzBuzz(15))
# Output: ['FizzBuzz', '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', \
# 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
