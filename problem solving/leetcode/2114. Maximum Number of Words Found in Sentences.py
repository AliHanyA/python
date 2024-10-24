class Solution(object):
    def mostWordsFound(self, sentences):
        tot = 0
        for x in sentences:
            words = x.split()
            tot = max(tot, len(words))

        return tot
