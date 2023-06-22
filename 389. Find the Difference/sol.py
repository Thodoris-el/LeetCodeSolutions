class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = 0
        for i in t:
            count += ord(i)
        for i in s:
            count -= ord(i)

        return chr(count)