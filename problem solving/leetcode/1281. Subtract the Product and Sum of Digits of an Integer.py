class Solution(object):
    def subtractProductAndSum(self, n):
            mult = 1
            sum = 0

            while n > 0:
                digit = n % 10
                mult *= digit
                sum += digit
                n //= 10

            return mult - sum
