class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        chisla = []
        s = 0
        for i in nums:
            s += i
            chisla.append(s)
        return chisla            