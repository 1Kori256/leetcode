class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        x = dividend // divisor
        if x > (2 ** 31) - 1:
            return (2 ** 31) - 1
        elif x < -1 * (2 ** 31):
            return -1 * (2 ** 31)
        elif x >= 0:
            return x
        elif dividend % divisor == 0:
            return x
        else:        
            return x + 1