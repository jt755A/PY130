def calculate_average(*nums):
    if nums:
        return sum(nums) / len(nums)

    return None


print(calculate_average()) # None
print(calculate_average(5, 6, 5)) # 5.33333
