class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 1+(num % 9) if num else 0