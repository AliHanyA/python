class Solution(object):
    def scoreOfString(self, s):
        res = 0
        for i in range(len(s) - 1):
            difference = abs(ord(s[i]) - ord(s[i + 1]))
            res += difference
        return res
