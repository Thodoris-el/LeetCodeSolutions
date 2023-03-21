class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        start = 0
        char = {}
        for i in range(len(s)):
            if s[i] in char:
                if char[s[i]] < start:
                    char[s[i]] = i
                else:
                    if i - start > length:
                        length = i - start
                    start = char[s[i]] + 1
                    char[s[i]] = i
            else:
                char[s[i]] = i
        if len(s) - start > length:
            length = len(s) - start
        return length
