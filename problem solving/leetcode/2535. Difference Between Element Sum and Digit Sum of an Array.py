class Solution(object):
    def differenceOfSum(self, nums):
        digit_sum = 0
        element_sum = sum(nums)
        for num in nums:
            while num > 0:
                digit_sum += num % 10
                num //= 10

        return abs(element_sum - digit_sum)
