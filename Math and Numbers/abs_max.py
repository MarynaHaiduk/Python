def abs_max(nums):
    max_el = abs(nums[0])
    for i in range(1, len(nums)):
        if abs(nums[i]) > max_el:
            max_el = abs(nums[i])
    return max_el

# Tests
print(abs_max([1, 2, -11]))  # 11
