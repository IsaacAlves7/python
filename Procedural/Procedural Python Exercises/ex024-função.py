def numberDistribution(nums):
    n = 0
    for x in range(len(nums)):
        for k in range(len(nums)+1):
            nums[x].append(n)
            n += 1
        n = nums[x][-1] + 1
    result = [N[::-1] for N in nums]
    return result
Numbers = [[] for _ in range(3)]
print(numberDistribution(Numbers))

# Output: [[3, 2, 1, 0], [7, 6, 5, 4], [11, 10, 9, 8]]