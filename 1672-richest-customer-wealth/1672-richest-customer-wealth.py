class Solution(object):
    def maximumWealth(self, accounts):
        m = 0
        for i in accounts:
            if sum(i) > m:
                m = sum(i)
        return m
        