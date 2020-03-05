# A set is a collection which is unordered and unindexed.
# The elements in the set cannot be duplicates.
# The elements in the set are immutable but the set as a whole is mutable.

s1, s2 = {1, 2, 3}, {4, 5, 6}
print(len(s1))       # set length
print(2 in s1)       # True/False if element in set
print(2 not in s1)   # True/False if element not in set
s1 <= s2             # True/False if each element in s1 is in s2 (or s1.issubset(s2))
s1 >= s2             # True/False if every element in s2 is in s1 (or s1.issuperset(s2))
s1.isdisjoint(s2)    # True/False if no common elements
print(s1.copy())     # return new set with a shallow copy of s1
s1 | s2              # union (все элементы из двух без повторов) (or s1.union(s2))
s1 & s2              # intersection (or s1.intersection(s2))
s1 - s2              # difference (or s1.difference(s2))
s1 ^ s2              # not in both (or s1.symmetric_difference(s2))
s1.add(25)           # add one item
s1.update({55, 45})  # add multiple items (or s1.update(s2))
s1 &= s2             # return s1 with elements also found in s2
                     # (or s1.intersection_update(s2))
s1 -= s2             # return s1 without elements found in s2
                     # (or s1.difference_update(s2))
s1 ^= s2             # return s1 with elements from s1 or s2 but not both
                     # (or s1.symmetric_difference_update(s2))
s1 |= s2
s1.discard(1)        # removes an element from s1 if present or will NOT raise an error
# s1.remove(2)       # removes an element or KeyError
s1.pop()             # removes an element or KeyError
# s1.clear()         # removes all the elements from the set
# del s1             # delete the set completely

# Access items
for i in s1:
    print(i, end=" ")
print()

# Create set
empty_set = set()    # empty set
s1 = {"one"}         # set with one element {'one'}
s2 = set('one')      # set from sequence {'n', 'o', 'e'}
s1 = {i*2 for i in range(10)}
s = set(("apple", "banana", "cherry"))
s = set(map(int, input().split()))
print(s, type(s))