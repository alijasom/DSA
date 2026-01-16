class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sumOfSquaresOfDigits(n):
            sum=0
            while n>0:
                dig=n%10
                sum=sum + (dig*dig)
                n=n/10
            return sum
        slow=n
        fast=n
        while n!= 1:
            slow = sumOfSquaresOfDigits(slow)
            fast=sumOfSquaresOfDigits(sumOfSquaresOfDigits(fast))
            if fast==1:
                return True
            if slow ==fast:
                return False
        return True
        