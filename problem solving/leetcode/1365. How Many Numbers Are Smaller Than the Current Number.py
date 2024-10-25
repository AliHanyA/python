class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = [0] * len(nums)
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    count += 1
            result[i] = count
        return result
