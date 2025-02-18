def find_missing_number(nums):
    n = len(nums) + 1
    missing = n
    for i, num in enumerate(nums):
        missing ^= num ^ (i + 1)
    return missing