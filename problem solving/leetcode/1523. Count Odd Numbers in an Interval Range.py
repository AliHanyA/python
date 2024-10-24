class Solution(object):
    def countOdds(self, low, high):
        x = (high + 1) // 2
        y = low // 2
        return x - y
        
