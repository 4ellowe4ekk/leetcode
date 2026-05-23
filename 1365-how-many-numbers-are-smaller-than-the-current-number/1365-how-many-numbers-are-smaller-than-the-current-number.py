class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        s = 0
        
        kolvo = []
        for i in nums:
            for j in nums:
                if i > j:
                    s += 1
            kolvo.append(s)
            s = 0
        return kolvo