# 1281. Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        for digit in str(n):
            product *= int(digit)
            sum += int(digit)
        return product - sum